from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from smartfit_booking.formatter import convert_24_to_12_hour
from smartfit_booking.logger import logger

import time

def initialize(driver_path: str, output_path: str, chrome_profile_path: str) -> object:
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=' + chrome_profile_path)
    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option("prefs", {
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.maximize_window()
    return driver

def login_to_website(driver: object, website_url: str, username: str, password: str) -> None:
    try:
        driver.get(website_url)
        username_field = driver.find_element_by_name('document')
        username_field.send_keys(username)
        password_field = driver.find_element_by_name('password')
        password_field.send_keys(password)
        login_button = driver.find_element_by_class_name('MuiButton-label')
        if login_button.text == 'INGRESAR':
            login_button.click()
        time.sleep(20)
        logger.info('Login to website has been successfully')
    except Exception as error:
        logger.error(f'Error to login to website: {error}')
        raise

def answer_questionnaire(driver: object) -> None:
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'MuiStepper-horizontal'))
        )
        next_button = driver.find_element_by_class_name('MuiButton-label')
        next_button.click()
        confirmation_modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'MuiDialog-container'))
        )
        confirm_button = confirmation_modal.find_element_by_class_name('MuiButton-containedPrimary')
        if confirm_button.text == 'CONFIRMAR':
            confirm_button.click()
        logger.info('Questionnaire has been answered successfully')
    except Exception as error:
        logger.error(f'Error to answer questionnaire: {error}')
        driver.quit()
        raise

def search_headquarter(driver: object, headquarter_name: str) -> None:
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'MuiCardContent-root'))
        )
        search_field = driver.find_element_by_class_name('MuiInputBase-input')
        search_field.send_keys(headquarter_name)
        search_field.send_keys(Keys.RETURN)
        headquarter_card = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'MuiGrid-item'))
        )
        select_button = headquarter_card.find_element_by_class_name('MuiButton-label')
        if select_button.text == 'SELECCIONAR':
            select_button.click()
        next_button = headquarter_card.find_element_by_class_name('MuiButton-label')
        if next_button.text == 'SIGUIENTE':
            next_button.click()
        logger.info('Headquarter has been searched successfully')
    except Exception as error:
        logger.error(f'Error to search headquarter: {error}')
        driver.quit()
        raise

def book_hour(driver: object, desired_date: str, desired_hour: str) -> None:
    try:
        input_date = driver.find_element_by_id('date-local')
        input_date.send_keys(Keys.CONTROL, 'a')
        input_date.send_keys(''.join(desired_date.split('/')))
        schedule_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'MuiTable-root'))
        )
        hours = schedule_table.find_elements_by_tag_name('tr')
        for hour in hours:
            h = hour.find_element_by_class_name('MuiTableCell-root')
            if h.text == desired_hour:
                book_button = hour.find_element_by_class_name('MuiButton-label')
                if book_button.text.startswith('RESERVAR'):
                    book_button.click()
        confirmation_modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'MuiDialog-container'))
        )
        confirm_button = confirmation_modal.find_element_by_class_name('MuiButton-containedPrimary')
        if confirm_button.text == 'CONFIRMAR':
            confirm_button.click()
        logger.info('Hour has been booked successfully')
    except Exception as error:
        logger.error(f'Error to book hour: {error}')
        driver.quit()
        raise

def get_qr_code(driver: object) -> str:
    try:
        qr_img = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'QRImg'))
        )
        qr_code_url = qr_img.get_attribute('src')
        time.sleep(10)
        logger.info('QR Code has been sent successfully')
        return qr_code_url
    except Exception as error:
        logger.error(f'Error to save QR Code: {error}')
        driver.quit()
        raise

def login_to_whatsapp(driver: object, whatsapp_url: str) -> None:
    try:
        driver.get(whatsapp_url) # Already authenticated
        logger.info(f'Login to WhatsApp Web has been successfully')
    except Exception as error:
        logger.error(f'Error to login in WhatsApp Web: {error}')
        driver.quit()
        raise

def search_chat(driver: object, chat_name: str) -> None:
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        search_box.clear()
        search_box.send_keys(chat_name)
        group_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//span[@title="{chat_name}"]'))
        )
        group_title.click()
        logger.info('Chat has been searched successfully')
    except Exception as error:
        logger.error(f'Error to search chat: {error}')
        driver.quit()
        raise

def send_message(driver: object, file_path: str, person_name: str, book_date: str, book_hour: str) -> None:
    try:
        # Send text
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]'))
        )
        input_box.send_keys(f'Código QR Reserva {book_date} a las {convert_24_to_12_hour(book_hour)} - {person_name}')
        input_box.send_keys(Keys.ENTER)

        # Attach file
        attachment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@title="Attach"]'))
        )
        attachment_box.click()
        image_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'))
        )
        image_box.send_keys(file_path)

        # Send file
        send_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@data-testid="send"]'))
        )
        send_button.click()
        time.sleep(10)
        logger.info('Message has been sent successfully')
    except Exception as error:
        logger.error(f'Error to send message: {error}')
        driver.quit()
        raise