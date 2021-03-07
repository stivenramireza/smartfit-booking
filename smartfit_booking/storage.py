import os

from smartfit_booking.logger import logger

def save_file(path: str, response: object) -> None:
    try:
        file = open(path, "wb")
        file.write(response.content)
        file.close()
        logger.info(f'File {path} has been saved successfully')
    except Exception as error:
        logger.error(f'Error to save image: {error}')
        raise

def remove_file(path: str) -> None:
    try:
        if os.path.exists(path):
            os.remove(path)
        logger.info(f'File {path} has been removed successfully')
    except Exception as error:
        logger.error(f'Error to remove file {path}: {error}')
        raise