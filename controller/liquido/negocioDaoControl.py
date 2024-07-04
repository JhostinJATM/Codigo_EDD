from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from model.liquido.negocio import Negocio 

class NegocioControl(DaoAdapter):
    def __init__(self):
        super().__init__(Negocio)
        self.__negocio = None

    def get_negocio(self):
        if self.__negocio == None:
            self.__negocio = Negocio()
        return self.__negocio

    def set_negocio(self, value):
        self.__negocio = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.get_negocio()._id = self._lista._length + 1
        self._save(self.get_negocio())
