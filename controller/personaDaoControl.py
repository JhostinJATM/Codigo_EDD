from typing import Type
from controller.dao.daoAdapterdb import DaoAdapter
from model.persona import Persona
import colorama

class PersonaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Persona)
        self.__persona = None

    @property
    def _persona(self):
        if self.__persona == None:
            self.__persona = Persona()
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _lista(self):
        return self._list()
    
    def merge(self, pos):
        self._merge(self._persona, pos)
    
    @property
    def save(self):
        try:
            self._save(self._persona)
            return True
        except Exception as e:
            print(colorama.Fore.GREEN + f"Error en save(personaDaoControl) es: {e}" + colorama.Fore.RESET)
            return False


