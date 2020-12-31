
from unittest import TestCase

from logger_multi_modules.SingleLogger import SingleLogger

class TestSingleLogger(TestCase):
    
    _name = "test.singlelogger"
    
    def setUp(self):
        try:
            self.log = SingleLogger(("%s.%s" %("Single Logging", __name__)), 0, "unified_logger.log", "../log/global/")
            self.assertIsInstance(self.log, SingleLogger, "Singleton Logger criado com sucesso")
        except:
            raise Exception
    
    
    def testGetInfoLevel(self):
        try:
            self.log.getInfoLevel()
            self.log.logger.info("Executed Log in Info Level")
        except:
            raise Exception

    
    def testGetDebugLevel(self):
        try:
            self.log.getDebugLevel()
            self.log.logger.debug("Executed Log in Debug Level")
        except:
            raise Exception

    
    def testGetWarningLevel(self):
        try:
            self.log.getWarningLevel()
            self.log.logger.warning("Executed Log in Warning Level")
        except:
            raise Exception
    
    
    def testGetCriticalLevel(self):
        try:
            self.log.getCriticalLevel()
            self.log.logger.critical("Executed Log in Critical Level")
        except:
            raise Exception
    
    
    def testGetErrorLevel(self):
        try:
            self.log.getErrorlLevel()
            self.log.logger.error("Executed Log in Error Level")
        except:
            raise Exception


    def tearDown(self):
        TestCase.tearDown(self)
        
    def doCleanups(self):
        return TestCase.doCleanups(self)



