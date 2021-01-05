# !/usr/bin/python3
# encoding: utf-8
'''
Created on 15 de dez de 2020
@author: Sandro Regis Cardoso | Engenheiro de Software
'''

import logging

LOGGER_TYPES = ["multmodules_log", "multthreads_log"]

class FactoryLoggerType(object):
    """
    Implement types of loggers:
    * multmodules_log
    * multthreads_log
    """
    _name = "logger.type"
    
    types = []
    
    def _template(self, logName = None, logLevel = None, logPath = None, logFile = None):
        """
        @description: Template method to create logging object
        @author: Sandro Regis Cardoso
        @TODO: Implement new types of logger
        @return: object
        """
        
        try:
            logger = logging.getLogger("%s" %(logName))
            formatter = logging.Formatter("%(asctime)s \t| %(name)s  \t\t| %(levelname)s |\t%(message)s")
            fileHandler = logging.FileHandler("%s%s" %(logPath, logFile))
            fileHandler.setFormatter(formatter)
            
            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(formatter)
        
            logger.setLevel(logLevel)
            logger.addHandler(fileHandler)
            logger.addHandler(streamHandler)
            
            #logger.info("%s.%s.%s" %(self._name, __name__, logLevel))
            return logger
        except:
            raise Exception
    
    
    #def __templateMultThreads(self, logName = None, logLevel = None, logFile = None, logPath = None):
    #    """
    #    @description: Template method to create logging object for mult thread programming 
    #    @author: Sandro Regis Cardoso
    #    @TODO: Implement new types of logger
    #    @return: object
    #    """
    #    try:
    #        pass
    #    except:
    #        raise Exception
    
    
    def createLogger(self, loggerType : str) -> logging:
        try:
            class FactoryGenericLogger(FactoryLoggerType):
                _name = "generic.logger"
                _description = "Create and return one logging object to record all events \
                                in a single log file"
                
                def getMultModulesLogger(self, logName : str, logLevel : logging, logPath : str, logFile : str) -> logging:
                    """
                    @author: Sandro Regis Cardoso
                    @TODO: 
                    @return: object
                    """
                    try:
                        multLogger = self._template(logName, logLevel, logPath, logFile)
                        return multLogger
                    except:
                        raise Exception
                
                
                #def getMultThreadsLogger(self, logName : str, logLevel : logging, logPath : str, logFile : str) -> logging:
                #    """
                #    @author: Sandro Regis Cardoso
                #    @TODO: 
                #    @return: object
                #    """
                #    try:
                #        pass
                #        #multThreads = self.__templateMultThreads(logName, logLevel, logPath, logFile)
                #        return
                #    except:
                #        raise Exception
            
            if loggerType == "multmodules_log":
                return FactoryGenericLogger()
            elif loggerType == "multthreads_log":
                pass
            assert 0, "Bad factory creation: %s" % type
        except:
            raise Exception
        
