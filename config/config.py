from loguru import logger
import os

if 'SAN_API_KEY' in os.environ.keys():
    api_key = os.environ['SAN_API_KEY']
else:
    logger.debug("No API key provided, quitting")
    raise EnvironmentError

shelve_dir = "persistence/shelf"
