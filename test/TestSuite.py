
import unittest
from unittest import TestSuite

from test.TestSingleLogger import TestSingleLogger
from test.TestMultLogger import TestMultLogger


def suite():
    suite = TestSuite()
    
    #TestSingleLogger
    suite.addTest(TestSingleLogger('testGetDebugLevel'))
    suite.addTest(TestSingleLogger('testGetInfoLevel'))
    suite.addTest(TestSingleLogger('testGetWarningLevel'))
    suite.addTest(TestSingleLogger('testGetCriticalLevel'))
    suite.addTest(TestSingleLogger('testGetErrorLevel'))
    
    #TestMultLogger
    suite.addTest(TestMultLogger('testGetDebugLevel'))
    suite.addTest(TestMultLogger('testGetInfoLevel'))
    suite.addTest(TestMultLogger('testGetWarningLevel'))
    suite.addTest(TestMultLogger('testGetCriticalLevel'))
    suite.addTest(TestMultLogger('testGetErrorLevel'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())