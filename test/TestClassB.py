import unittest
from unittest import TestCase

from models.ClasseB import ClasseB

class TestClasseB(TestCase):

    def setUp(self):
        try:
            self.objB = ClasseB()
        except:
            raise Exception
    

    def tearDown(self):
        del(self.objB)

    def testmethodB1(self):
        try:
            self.objB.methodB1()
        except:
            raise Exception
        
    
    def testmethodB2(self):
        try:
            self.objB.methodB2()
        except:
            raise Exception


"""  

"""
if __name__ == '__main__':
    unittest.main()