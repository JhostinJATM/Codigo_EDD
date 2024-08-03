from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from model.liquido.negocio import Negocio 

class NegocioControl(DaoAdapter):
    def __init__(self):
        super().__init__(Negocio)
        self.__negocio = None

    @property
    def _negocio(self):
        if self.__negocio == None:
            self.__negocio = Negocio()
        return self.__negocio

    @_negocio.setter
    def _negocio(self, value):
        self.__negocio = value

    @property
    def _lista(self):
        return self._list()
    
    def merge(self, pos):
        self._merge(self._negocio, pos)
    
    @property
    def save(self):
        try:
            self._negocio._id = self._lista._length + 1
            self._save(self._negocio)
            return True
        except Exception as e:
            print(f"Error en save es: {e}")
            return False

