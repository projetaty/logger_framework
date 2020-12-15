#!/usr/bin/python3
# encoding: utf-8
'''
Created on 15 de dez de 2020
@author: Sandro Regis Cardoso | Engenheiro de Software
'''

class MultiModules():
    
    def __init__(self):
        self.name = "MultiModules"
        return
    
class MultiThread():
    
    def __init__(self):
        self.name = "MultiThread"
        return


class Adapter:
    """
    Adata um objeto ao substituir metodos.
    Uso:
    multiModule = MultiModule()
    multiModule = Adapter(multiModule, makeLogger=None)
    """
    def __init__(self, obj, **adapted_methods):
        """Set the adapted methods in an object's"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """Todas chamadas nao apdated sao enviadas para o objeto"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__


