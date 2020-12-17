# !/usr/bin/python3
# encoding: utf-8
'''
Created on 15 de dez de 2020
@author: Sandro Regis Cardoso | Engenheiro de Software
@reference: https://docs.python.org/3/howto/logging-cookbook.html#
'''

import logging
import threading
import time

def worker(arg):
    while not arg['stop']:
        logging.debug('Hi from method worker')
        time.sleep(1.5)

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
    info = {'stop': False}
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()
    while True:
        try:
            logging.debug('Hello from main')
            time.sleep(1.75)
        except KeyboardInterrupt:
            info['stop'] = True
            break
    thread.join()


if __name__ == '__main__':
    main()





