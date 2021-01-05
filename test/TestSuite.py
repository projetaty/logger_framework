

"""
@TODO: Make this suite a little bit more elegant
@author: Sandro Regis Cardoso | Engenheiro de Software
"""
import unittest
from unittest import TestSuite

from test.TestSingleLogger import TestSingleLogger
from test.TestMultLogger import TestMultLogger
from test.TestClassA import TestClasseA


def suiteTestSingleLogger():
    suite = TestSuite()
    print("\nSuite Test running Unified Logger (Singleton Pattern):")
    suite.addTest(TestSingleLogger('testGetDebugLevel'))
    suite.addTest(TestSingleLogger('testGetInfoLevel'))
    suite.addTest(TestSingleLogger('testGetWarningLevel'))
    suite.addTest(TestSingleLogger('testGetCriticalLevel'))
    suite.addTest(TestSingleLogger('testGetErrorLevel'))
    return suite


def suiteTestClassSingleLogger():
    suite = TestSuite()
    print("\nSuite Test running Unified Logger with Class Model (Singleton Pattern):")
    suite.addTest(TestClasseA('testmethodA1'))
    suite.addTest(TestClasseA('testmethodA2'))
    return suite


def suiteTestMultLogger():
    suite = TestSuite()
    print("\nSuite Test running Multi Logger (Factory Pattern):")
    suite.addTest(TestMultLogger('testGetDebugLevel'))
    suite.addTest(TestMultLogger('testGetInfoLevel'))
    suite.addTest(TestMultLogger('testGetWarningLevel'))
    suite.addTest(TestMultLogger('testGetCriticalLevel'))
    suite.addTest(TestMultLogger('testGetErrorLevel'))
    return suite


if __name__ == '__main__':
    suite = TestSuite()
    
    #initialize suite runner
    runner = unittest.TextTestRunner()
    
    #TestSingleLogger
    #runner.run(suiteTestSingleLogger())
    
    #TestClassA
    runner.run(suiteTestClassSingleLogger())
    
    #TestMultLogger
    #runner.run(suiteTestMultLogger())