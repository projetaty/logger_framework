
import unittest
from unittest import TestSuite

from test.TestLoggerMultModules import TestLoggerMultModules



def suite():
    suite = TestSuite()
    suite.addTest(TestLoggerMultModules('testGetDebugLevel'))
    suite.addTest(TestLoggerMultModules('testGetInfoLevel'))
    suite.addTest(TestLoggerMultModules('testGetWarningLevel'))
    suite.addTest(TestLoggerMultModules('testGetCriticalLevel'))
    suite.addTest(TestLoggerMultModules('testGetErrorLevel'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())