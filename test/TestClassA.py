#!/usr/bin/python3.7

import unittest
from unittest import TestCase

from models.ClasseA import ClasseA
import os

class TestClasseA(TestCase):
    
    objA = ClasseA()
    
    
    def testMethodA1(self):
        try:
            self.objA.methodA1()
        except:
            raise Exception
    
    
    def testMethodA2(self):
        try:
            self.objA.methodA2()
        except:
            raise Exception
    
    
    def testMethodAB(self):
        try:
            self.objA.methodAB()
        except:
            raise Exception
    
