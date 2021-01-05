import unittest
from unittest import TestCase

from models.ClasseA import ClasseA

class TestClasseA(TestCase):

    def setUp(self):
        try:
            self.objA = ClasseA()
        except:
            raise Exception
    

    def tearDown(self):
        del(self.objA)

    def testmethodA1(self):
        try:
            self.objA.methodA1()
        except:
            raise Exception
        
    
    def testmethodA2(self):
        try:
            self.objA.methodA2()
        except:
            raise Exception
        

if __name__ == '__main__':
    unittest.main()