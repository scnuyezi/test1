import logging,logging.config,sys

CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logger=logging.getLogger()

logging.info('test333')

# print(sys.path)TimedRotatingFileHandler