from secrets import (
    DRIVER_PATH,
    OUTPUT_PATH,
    WEBSITE_URL,
    IDENTIFICATION,
    PASSWORD,
    HEADQUARTER_NAME,
    DESIRED_TIME,
    WHATSAPP_URL,
    CHAT_NAME,
    PERSON_NAME,
    CHROME_PROFILE_PATH
)

from smartfit_booking.website_bot import (
    initialize,
    login_to_website,
    answer_questionnaire,
    search_headquarter,
    book_hour,
    get_qr_code,
    login_to_whatsapp,
    search_chat,
    send_message
)

from smartfit_booking.storage import (
    save_file,
    remove_file
)

from smartfit_booking.data_access_api import get_data

import os

def main():
    """ book_an_hour """
    driver = initialize(DRIVER_PATH, OUTPUT_PATH, CHROME_PROFILE_PATH)
    login_to_website(driver, WEBSITE_URL, IDENTIFICATION, PASSWORD)
    answer_questionnaire(driver)
    search_headquarter(driver, HEADQUARTER_NAME)
    book_hour(driver, DESIRED_TIME)
    qr_code_url = get_qr_code(driver)

    """ download_qr_code """
    response = get_data(qr_code_url)
    image_path = os.path.join(OUTPUT_PATH, 'code.jpg')
    save_file(image_path, response)

    """ send_whatsapp_message """
    login_to_whatsapp(driver, WHATSAPP_URL)
    search_chat(driver, CHAT_NAME)
    send_message(driver, image_path, PERSON_NAME, DESIRED_TIME)
    remove_file(image_path)

if __name__ == '__main__':
    main()