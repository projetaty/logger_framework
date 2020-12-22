#!/usr/bin/python3
# encoding: utf-8
'''
Created on 17 de dez. de 2020
@author: Sandro Regis Cardoso | Software Engineer
@email: projetaty@gmail.com
@module: logger_multi_modules.test.TestLogMultModules
'''

import unittest
from unittest import TestCase

from utils.FactoryLogger import FactoryLoggerType
import logging

class TestCase(TestCase):

    logger = None
    
    def setUp(self):
        try:
            logType = FactoryLoggerType()
            res = logType.createLogger("multmodules_log")
            self.logger = res.getMultModulesLogger(logName = "Logger_Factory", logLevel = logging.INFO, 
                                              logFile = "test_factory.log", logPath = "../log/")
            return self.logger
        except:
            self.logger.exception(Exception)
            raise Exception

    def tearDown(self):
        unittest.TestCase.tearDown(self)


class TestLogMultModules(TestCase):
    
    _name = "test.log.multmod"
    _description = "Class to test mult-modules logger"
    
    """def setUp(self):
        try:
            unittest.TestCase.setUp(self)
        except:
            raise Exception"""
    
    def testLoggerDebugLevel(self):
        """
        Decription:
        @author: Sandro Regis Cardoso
        @TODO: 
        @return: Boolean
        """
        try:
            self.logger.setLevel(logging.DEBUG)
            self.logger.debug('\tLogging Debug message')
        except:
            self.logger.exception(Exception)
            raise Exception
    
    
    def testLoggerWarningLevel(self):
        """
        Decription:
        @author: Sandro Regis Cardoso
        @TODO: 
        @return: Boolean
        """
        try:
            self.logger.setLevel(logging.WARNING)
            self.logger.warning('\tLogging Warning message')
        except:
            self.logger.exception(Exception)
            raise Exception
    
    
    def testLoggerInfoLevel(self):
        """
        Decription:
        @author: Sandro Regis Cardoso
        @TODO: 
        @return: Boolean
        """
        try:
            self.logger.setLevel(logging.INFO)
            self.logger.info("\tLogging Info Message")
        except:
            self.logger.exception(Exception)
            raise Exception
    
    
    def testLoggerCriticalLevel(self):
        """
        Decription:
        @author: Sandro Regis Cardoso
        @TODO: 
        @return: Boolean
        """
        try:
            self.logger.setLevel(logging.CRITICAL)
            self.logger.critical('\tLogging Critical message')
        except:
            self.logger.exception(Exception)
            raise Exception
    
    def testLoggerErrorLevel(self):
        """
        Decription:
        @author: Sandro Regis Cardoso
        @TODO: 
        @return: Boolean
        """
        try:
            self.logger.setLevel(logging.ERROR)
            self.logger.error('\tLogging Error message')
        except:
            self.logger.exception(Exception)
            raise Exception

    def tearDown(self):
        return TestCase.tearDown(self)
        
    def doCleanups(self):
        return TestCase.doCleanups(self)
    

if __name__ == '__main__':
    unittest.main()

