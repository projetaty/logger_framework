'''
Created on 26 de dez de 2020
@author: samurai
'''

import logging
from utils.FactoryLogger import FactoryLoggerType, LOGGER_TYPES

class MultLoggers(object):
    _name = "mult.loggers"
    
    def __init__(self, logName : str, logLevel : logging, logPath : str, logFile : str):
        try:
            logType = FactoryLoggerType()
            logInstance = logType.createLogger(LOGGER_TYPES[0])
            self.logger = logInstance.getMultModulesLogger(logName = logName, logLevel = logLevel, logPath = logPath, logFile = logFile)
        except:
            raise Exception
    
    
    def getInfoLevel(self):
        """
        Decription: Set logger to Info Level
        @author: Sandro Regis Cardoso
        @TODO: 
        @return: Boolean
        """
        try:
            self.logger.setLevel(logging.INFO)
            self.logger.info("Setting Log Info Level")
        except:
            #self.logger.exception(Exception)
            raise Exception
    
    
    def getDebugLevel(self):
        """
        Decription: Set logger to Debug Level
        @author: Sandro Regis Cardoso
        @TODO: 
        @return: Boolean
        """
        try:
            self.logger.setLevel(logging.DEBUG)
            self.logger.debug('Setting Log Debug Level')
        except:
            self.logger.exception(Exception)
            raise Exception
    
    
    def getWarningLevel(self):
        """
        Decription: Set logger to Warning Level
        @author: Sandro Regis Cardoso
        @TODO: 
        @return: Boolean
        """
        try:
            self.logger.setLevel(logging.WARNING)
            self.logger.warning('Setting Log Warning Level')
        except:
            self.logger.exception(Exception)
            raise Exception
    
        
    def getCriticalLevel(self):
        """
        Decription: Set logger to Critical Level
        @author: Sandro Regis Cardoso
        @TODO: 
        @return: Boolean
        """
        try:
            self.logger.setLevel(logging.CRITICAL)
            self.logger.critical('Setting Log Critical Level')
        except:
            self.logger.exception(Exception)
            raise Exception


    def getErrorlLevel(self):
        """
        Decription: Set logger to Error Level
        @author: Sandro Regis Cardoso
        @TODO: 
        @return: Boolean
        """
        try:
            self.logger.setLevel(logging.ERROR)
            self.logger.error('Setting Log Error Level')
        except:
            self.logger.exception(Exception)
            raise Exception


