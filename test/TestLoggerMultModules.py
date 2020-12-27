
from unittest import TestCase
from logger_multi_modules.LoggerMultModules import LoggerMultModules

class TestLoggerMultModules(TestCase):
    
    _name = "testlogger.multmodules"
    
    def setUp(self):
        try:
            self.log = LoggerMultModules("%s.%s" %("Logging Global", __name__), 0, "test2_logger_mult_modules.log",  "../log/")
            self.assertIsInstance(self.log, LoggerMultModules)
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
            self.logError = LoggerMultModules("%s.%s" %("Logging Error", __name__), 0, "error_logger_mult_modules.err",  "../err/")
            self.assertIsInstance(self.log, LoggerMultModules)
            self.logError.getErrorlLevel()
            self.logError.logger.error("Executed Log in Error Level")
        except:
            raise Exception


    def tearDown(self):
        TestCase.tearDown(self)
        
    def doCleanups(self):
        return TestCase.doCleanups(self)



"""def main():
    unittest.main()

if __name__ == '__main__':
    main()"""



