from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from model.persona import Persona
from config.logging_config import log
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
            # log.debug(colorama.Fore.RED + f"iD: {self._lista._length}" + colorama.Fore.RESET)
            # self._persona._id = self._lista._length + 1
            # log.info(colorama.Fore.BLUE + f"nuevo id = {self._persona._id}" + colorama.Fore.RESET)
            self._save(self._persona)
            return True
        except Exception as e:
            log.debug(colorama.Fore.GREEN + f"Error en save(personaDaoControl) es: {e}" + colorama.Fore.RESET)
            return False


