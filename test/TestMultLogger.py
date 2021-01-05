
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
            log = self.__getLoggerInstance("Debug", logging.DEBUG, "../log/debug/", "test_debug_logger.log")
            #log.getDebugLevel()
            log.logger.debug("Executed Log in Debug Level")
            del(log)
        except:
            raise Exception
    
    
    def testGetInfoLevel(self):
        try:
            log = self.__getLoggerInstance("Info", logging.INFO, "../log/info/", "test_info_logger.log")
            #log.getInfoLevel()
            log.logger.info("Executed Log in Info Level")
            del(log)
        except:
            raise Exception

    
    def testGetWarningLevel(self):
        try:
            log = self.__getLoggerInstance("Warning", logging.WARNING, "../log/warn/", "test_warning_logger.log")
            #log.getWarningLevel()
            log.logger.warning("Executed Log in Warning Level")
            del(log)
        except:
            raise Exception
    
    
    def testGetCriticalLevel(self):
        try:
            log = self.__getLoggerInstance("Critical", logging.CRITICAL, "../log/critical/", "test_critical_logger.log")
            #log.getCriticalLevel()
            log.logger.critical("Executed Log in Critical Level")
            del(log)
        except:
            raise Exception
    
    def testGetErrorLevel(self):
        try:
            log = self.__getLoggerInstance("Error", logging.ERROR, "../log/error/", "test_error_logger.err")
            #log.getErrorlLevel()
            log.logger.error("Executed Log in Error Level")
            del(log)
        except:
            raise Exception

    def tearDown(self):
        TestCase.tearDown(self)
        
    def doCleanups(self):
        return TestCase.doCleanups(self)





