# !/usr/bin/python3
# encoding: utf-8
'''
Created on 15 de dez de 2020
@author: Sandro Regis Cardoso | Engenheiro de Software
@reference: https://docs.python.org/3/howto/logging-cookbook.html#
'''

import logging


class LoggerSingleton(type):
    _instances = {}
    
    def __init__(cls : type, name : str, bases, dict : dict) -> type:
        print("bases %s\n\n\n" %bases)
        super(LoggerSingleton, cls).__init__(name, bases, dict)
        original_new = cls.__new__
        
        def objecInstance(cls, *args, **kwds):
            if cls.instance == None:
                cls.instance = original_new(cls, *args, **kwds)
            return cls.instance
        
        cls.instance = None
        cls.__new__ = staticmethod(objecInstance)


class LoggerManager(object):
    __metaclass__ = LoggerSingleton
    
    _loggers = {}
    
    def __init__(self, *args, **kwargs):
        pass
    
    @staticmethod
    def getLogger(name=None):
        if not name:
            logging.basicConfig()
            return logging.getLogger()
        elif name not in LoggerManager._loggers.keys():
            logging.basicConfig()
            LoggerManager._loggers[name] = logging.getLogger(str(name))
        return LoggerManager._loggers[name]

