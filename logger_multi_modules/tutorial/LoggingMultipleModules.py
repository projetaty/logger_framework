# !/usr/bin/python3
# encoding: utf-8

#tutorial: https://docs.python.org/3/howto/logging-cookbook.html#

import logging
from utils.SingletonLogger import LoggerManager
from logger_multi_modules.tutorial import AuxiliaryModule

# create logger with 'spam_application'
logger = LoggerManager.getLogger("LoggerFrameworkApp")
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
objFileHandler = logging.FileHandler('./log/multiple_modules.log')
objFileHandler.setLevel(logging.DEBUG)

# create file handler whith objErrorHandler logs even debug messages
objErrorHandler = logging.StreamHandler()
objErrorHandler.setLevel(logging.ERROR)

# create formatter and add it to the handlers
logFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
objFileHandler.setFormatter(logFormat)
objErrorHandler.setFormatter(logFormat)

# add the handlers to the logger
logger.addHandler(objFileHandler)
logger.addHandler(objErrorHandler)

logger.info('creating an instance of AuxiliaryModule.Auxiliary')
objAuxiliar = AuxiliaryModule.Auxiliary()
logger.info('created an instance of AuxiliaryModule.Auxiliary')
logger.info('calling AuxiliaryModule.Auxiliary.do_something')

objAuxiliar.do_something()
logger.info('finished AuxiliaryModule.Auxiliary.do_something')
logger.info('calling AuxiliaryModule.some_function()')

AuxiliaryModule.some_function()
logger.info('done with AuxiliaryModule.some_function()')

