import requests

from smartfit_booking.logger import logger

def get_data(url: str) -> object:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logger.info(f'Data has been gotten successfully')
            return response
    except Exception as error:
        logger.error(f'Error to get data from url {url}: {error}')
        raise