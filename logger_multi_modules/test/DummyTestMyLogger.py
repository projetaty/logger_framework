'''
Created on 15 de dez de 2020
@author: Sandro Regis Cardoso | Engenheiro de Software
@reference: https://docs.python.org/3/howto/logging-cookbook.html#
'''
from utils.SingletonLogger import LoggerManager
import logging

class TestMyLogger(object):
    
    _name = "test.mylogger"
    
    def __init__(self):
        try:
            # create logger with 'spam_application'
            self.logger = LoggerManager.getLogger("LoggerFrameworkApp")
            self.logger.setLevel(logging.DEBUG)
            # create console handler with a higher log level
            objFileHandler = logging.FileHandler('../log/multiple_modules.log')
            objFileHandler.setLevel(logging.DEBUG)
            
            # create file handler whith objErrorHandler logs even debug messages
            objErrorHandler = logging.StreamHandler()
            objErrorHandler.setLevel(logging.ERROR)
            
            # create formatter and add it to the handlers
            logFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            objFileHandler.setFormatter(logFormat)
            objErrorHandler.setFormatter(logFormat)
            
            # add the handlers to the logger
            self.logger.addHandler(objFileHandler)
            self.logger.addHandler(objErrorHandler)
            
            self.logger.info("Sistema inicializado.....")
        except:
            self.logger.exception(Exception)
            raise Exception
        
        
    def do(self, param):
        self.logger.info("parametro do metodo do() : %s " %param)
        self.logger.info("EXECUTANDO METODO DO()")

t1 = None
try:
    t1 = TestMyLogger()
    t1.logger.info("objeto da classe TestMyLogger criado...")
    t1.do("faz algum trein")
except:
    t1.logger.exception("Error on processing some task {}".format(BaseException.message))
    raise BaseException


