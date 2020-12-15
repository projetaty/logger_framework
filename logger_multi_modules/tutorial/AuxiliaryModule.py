#import logging
from utils.SingletonLogger import LoggerManager
# create logger
module_logger = LoggerManager.getLogger('Auxiliary')

class Auxiliary:

    def __init__(self):
        self.logger = LoggerManager.getLogger('LoggerFrameworkApp.AuxiliaryModule.Auxiliary')
        self.logger.info('creating an instance of Auxiliary')

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')

def some_function():
    module_logger.info('received a call to "some_function"')
