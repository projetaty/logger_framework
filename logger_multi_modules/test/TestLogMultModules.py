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

from utils.SingletonLogger import LoggerManager
import logging

class TestCase(TestCase):

    """def setUp(self):
        try:
            pass
        except:
            raise Exception"""

    def tearDown(self):
        unittest.TestCase.tearDown(self)


class TestLogMultModules(TestCase):
    
    _name = "test.log.multmod"
    _description = "Class to test mult-modules logger"
    
    
    def setUp(self):
        try:
            # create logger with 'spam_application'
            self.logger = LoggerManager.getLogger("LoggerFrameworkApp")
            #self.logger.setLevel(logging.DEBUG)
            
            # create console handler with a higher log level
            objFileHandler = logging.FileHandler('../log/test_log_mult_modules.log')
            objFileHandler.setLevel(logging.DEBUG)
            with open('../log/test_log_mult_modules.log', 'r') as f:
                res = f.read()
                self.assertNotEqual(res, None)
            
            # create file handler whith objErrorHandler logs with debug messages
            objErrorHandler = logging.StreamHandler()
            objErrorHandler.setLevel(logging.ERROR)
            
            # create file handler whith objErrorHandler logs with warning messages
            objWarningHandler = logging.StreamHandler()
            objWarningHandler.setLevel(logging.WARNING)
            
            # create file handler whith objInfoHandler logs with info messages
            objInfoHandler = logging.StreamHandler()
            objInfoHandler.setLevel(logging.INFO)
            
            # create file handler whith objCriticalHandler logs with critical messages
            objCriticalHandler = logging.StreamHandler()
            objCriticalHandler.setLevel(logging.CRITICAL)
            
            # create formatter and add it to the handlers
            logFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            objFileHandler.setFormatter(logFormat)
            objErrorHandler.setFormatter(logFormat)
            objWarningHandler.setFormatter(logFormat)
            objInfoHandler.setFormatter(logFormat)
            objCriticalHandler.setFormatter(logFormat)
            
            # add the handlers to the logger
            self.logger.addHandler(objFileHandler)
            #self.logger.addHandler(objInfoHandler)
            #self.logger.addHandler(objWarningHandler)
            #self.logger.addHandler(objCriticalHandler)
            
            #self.logger.msg("TestCase running.......")
            
        except:
            self.logger.exception(Exception)
            raise Exception
    
    
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
            raise Exception

    def tearDown(self):
        return TestCase.tearDown(self)
        
    def doCleanups(self):
        return TestCase.doCleanups(self)
    

if __name__ == '__main__':
    unittest.main()

