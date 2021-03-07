from dotenv import load_dotenv

from smartfit_booking.logger import logger

import os

ENV = os.environ.get('ENV')
if ENV == 'production':
    dotenv_path = '.env'
    logger.info('Using production environment variables')
else:
    dotenv_path = '.env.dev'
    logger.info('Using development environment variables')

exists = os.path.exists(dotenv_path)

if not exists:
    raise Exception('env files do not exist')

load_dotenv(dotenv_path)

DRIVER_PATH = os.environ.get('DRIVER_PATH')
OUTPUT_PATH = os.environ.get('OUTPUT_PATH')
WEBSITE_URL = os.environ.get('WEBSITE_URL')
IDENTIFICATION = os.environ.get('IDENTIFICATION')
PASSWORD = os.environ.get('PASSWORD')
HEADQUARTER_NAME = os.environ.get('HEADQUARTER_NAME')
DESIRED_TIME = os.environ.get('DESIRED_TIME')
WHATSAPP_URL = os.environ.get('WHATSAPP_URL')
CHAT_NAME = os.environ.get('CHAT_NAME')
PERSON_NAME = os.environ.get('PERSON_NAME')
CHROME_PROFILE_PATH = os.environ.get('CHROME_PROFILE_PATH')