#!/usr/bin/python3.7

from logger_multi_modules.SingleLogger import SingleLogger
import logging

class ClasseB(object):
    '''
    classdocs
    '''
    _name = "classe.b"
    _description = "Dummy python class"
    
    def __init__(self):
        """
        Initialize log instance on level info
        @author: Sandro Regis Cardoso
        """
        try:
            self.logB = SingleLogger(("%s.%s" %("Single Logging Mult Modules", __name__)), logging.INFO, "../log/global/", "classeB_logger.log").logger
            self.logErrorB = SingleLogger(("%s.%s" %("Single Logging Mult Modules", __name__)), logging.ERROR, "../log/global/", "classeB_logger.log").logger
        except:
            raise Exception
    
    
    def methodB1(self):
        """
        Description: Dummy method for class B
        @author: Sandro Regis Cardoso
        @TODO: 
        @return: Boolean
        """
        try:
            self.logB.info("running method B1")
        except:
            self.logErrorB.exception("error running method B1 %s\n\n" %Exception)
            raise Exception
    
    def methodB2(self):
        """
        Description: Dummy method for class B
        @author:   Sandro Regis Cardoso
        @TODO:     
        @return:   Boolean
        """
        try:
            self.logB.info("running method B2")
        except:
            self.logErrorB.exception("error running method B2 %s\n\n" %Exception)
            raise Exception
        
