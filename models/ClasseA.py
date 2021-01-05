#!/usr/bin/python3.7

from logger_multi_modules.SingleLogger import SingleLogger
import logging

class ClasseA(object):
    '''
    classdocs
    '''
    _name = "classe.a"
    _description = "Dummy python class"
    
    def __init__(self):
        """
        Initialize log instance on level info
        @author: Sandro Regis Cardoso
        """
        try:
            self.log = SingleLogger(("%s.%s" %("Single Logging", __name__)), 0, "../log/global/", "classeA_logger.log").logger
            
            self.logERROR = SingleLogger(("%s.%s" %("Single Logging", __name__)), 0, "../log/global/", "classeA_logger.log").logger
            self.logERROR.setLevel(logging.ERROR)
        except:
            raise Exception
    
    
    def methodAB(self):
        try:
            self.log = SingleLogger(("%s.%s" %("Single Logging AB", __name__)), 0, "../log/global/", "classeAB_logger.log").logger
            
            self.log.setLevel(logging.INFO)
            self.log.info("....running INFO LEVEL on method AB")
            
            
            self.log.setLevel(logging.DEBUG)
            self.log.debug("....running DEBUG LEVEL on method AB")
            
            
            self.log.setLevel(logging.CRITICAL)
            self.log.critical("....running CRITICAL LEVEL on method AB")
            
            
            self.log.setLevel(logging.WARNING)
            self.log.warning("....running WARNING LEVEL on method AB")
            
            
            self.log.setLevel(logging.ERROR)
            self.log.error("....running ERROR LEVEL on method AB")
            
        except:
            raise Exception
    
    
    def methodA1(self):
        """
        Description: Dummy method for class A
        @author: Sandro Regis Cardoso
        @return: Boolean
        @TODO: 
        """
        try:
            self.log.setLevel(logging.INFO)
            self.log.info("running method A1")
        except:
            self.logERROR.exception("error running method A1 %s\n\n" %Exception)
            raise Exception
    
    def methodA2(self):
        """
        Description: Dummy method for class A
        @author:   Sandro Regis Cardoso
        @return:   Boolean
        @TODO:     
        """
        try:
            self.log.setLevel(logging.INFO)
            self.log.info("running method A2")
        except:
            self.logERROR.exception("error running method A2 %s\n\n" %Exception)
            raise Exception
