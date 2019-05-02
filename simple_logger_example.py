import logging

LOG_FORMAT = '%(asctime)s %(filename)-15s:%(lineno)s %(funcName)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.WARNING, format=LOG_FORMAT)
logger = logging.getLogger()

# Show when level logging.warning, logging.info, logging.debug
logger.warn('WARNING')

# Show when level logging.info, logging.debug
logger.info('INFO')

# Show when level logging.debug
logger.debug('DEBUG')