'''
Created on 26 de dez de 2020

@author: samurai
'''

import logging
from utils.SingletonLogger import LoggerManager

class SingleLogger(object):
    _name = "single.looger"
    
    def __init__(self, logName : str, logLevel : logging, logFile : str, logPath : str):
        try:
            self.logger = LoggerManager.getLogger(logName)
            self.logger.setLevel(logLevel)
            objFileHandler = logging.FileHandler("%s%s" %(logPath, logFile)) #'../log/global/unified_logger.log')
            logFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            objFileHandler.setFormatter(logFormat)
            self.logger.addHandler(objFileHandler)
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


