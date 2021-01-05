#!/usr/bin/python3.7

import unittest
from unittest import TestCase

from models.ClasseB import ClasseB


class TestClasseB(TestCase):
    
    objB = ClasseB()

    def testMethodB1(self):
        try:
            self.objB.methodB1()
        except:
            raise Exception
    
    
    def testMethodB2(self):
        try:
            self.objB.methodB2()
        except:
            raise Exception

    
    def testMethodBA(self):
        try:
            self.objB.methodBA()
        except:
            raise Exception
    


