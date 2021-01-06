'''
Created on 26 de dez de 2020

@author: samurai
'''

import logging
import logging.handlers as handlers
from utils.SingletonLogger import LoggerManager
import datetime
import time

class SingleLogger(object):
    _name = "single.logger"
    
    
    def __init__(self, logName : str, logLevel : logging, logPath : str, logFile : str):
        try:
            self.logger = LoggerManager.getLogger(logName)
            self.logger.setLevel(logLevel)
            objFileHandler = logging.FileHandler("%s%s" %(logPath, logFile))
            logFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            objFileHandler.setFormatter(logFormat)
            self.logger.addHandler(objFileHandler)
            
            """objTimeRotate  = handlers.TimedRotatingFileHandler(logFile, when="M", interval=1, atTime=datetime.time())
            current_time = int(time.time())
            rollover_time = objTimeRotate.computeRollover(current_time)
            self.logger.addHandler(rollover_time)"""
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
            level = self.logger.setLevel(logging.INFO)
            self.logger.info("\t\tSetting Log to Info  Level")
            return level
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
            self.logger.debug('\t\tSetting Log to Debug Level')
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
            self.logger.warning('\tSetting Log to Warning  Level')
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
            self.logger.critical('\tSetting Log to Critical Level')
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
            self.logger.error('\t\tSetting Log to Error Level')
        except:
            self.logger.exception(Exception)
            raise Exception


"""  
sl = SingleLogger(("%s.%s" %("\tSingle Logging", __name__)), logging.INFO, logPath = "../log/global/", logFile = "test_classeAB_logger.log")
sl.getWarningLevel()
sl.getCriticalLevel()
sl.getDebugLevel()
sl.getInfoLevel()
sl.getErrorlLevel()
"""