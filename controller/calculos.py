import os
import sys

sys.path.append('../')

from model.mru import MRU

class Calculos:
    def __init__(self):
        self.__mru = MRU()

    @property
    def _mru(self):
        return self.__mru

    @_mru.setter
    def _mru(self, value):
        self.__mru = value

    #*TODO
    def calcular_velocidad(self):
        self._mru._velocidad = self._mru._distancia / self._mru._tiempo
        return self._mru._velocidad 
    