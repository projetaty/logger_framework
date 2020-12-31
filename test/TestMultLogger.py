
from unittest import TestCase
from logger_multi_modules.MultLoggers import MultLoggers
import logging

class TestMultLogger(TestCase):
    
    _name = "test.multloggers"
    
    def setUp(self):
        TestCase.setUp(self)
    
        
    def __getLoggerInstance(self, logName : str, logLevel : logging, fileName : str, filePath : str) -> MultLoggers:
        try:
            log = MultLoggers("%s %s.%s" %("Logging ", logName, __name__), logLevel, fileName,  filePath)
            self.assertIsInstance(log, MultLoggers)
            return log
        except:
            raise Exception
    
    
    def testGetDebugLevel(self):
        try:
            log = self.__getLoggerInstance("Debug", logging.DEBUG, "test_debug_logger.log", "../log/debug/")
            #log.getDebugLevel()
            log.logger.debug("Executed Log in Debug Level")
            del(log)
        except:
            raise Exception
    
    
    def testGetInfoLevel(self):
        try:
            log = self.__getLoggerInstance("Info", logging.INFO, "test_info_logger.log", "../log/info/")
            #log.getInfoLevel()
            log.logger.info("Executed Log in Info Level")
            del(log)
        except:
            raise Exception

    
    def testGetWarningLevel(self):
        try:
            log = self.__getLoggerInstance("Warning", logging.WARNING, "test_warning_logger.log", "../log/warn/")
            #log.getWarningLevel()
            log.logger.warning("Executed Log in Warning Level")
            del(log)
        except:
            raise Exception
    
    
    def testGetCriticalLevel(self):
        try:
            log = self.__getLoggerInstance("Critical", logging.CRITICAL, "test_critical_logger.log", "../log/critical/")
            #log.getCriticalLevel()
            log.logger.critical("Executed Log in Critical Level")
            del(log)
        except:
            raise Exception
    
    def testGetErrorLevel(self):
        try:
            log = self.__getLoggerInstance("Error", logging.ERROR, "test_error_logger.err", "../log/error/")
            #log.getErrorlLevel()
            log.logger.error("Executed Log in Error Level")
            del(log)
        except:
            raise Exception

    def tearDown(self):
        TestCase.tearDown(self)
        
    def doCleanups(self):
        return TestCase.doCleanups(self)





