
import json
from model.persona import Persona
from controller.tda.linked.linkedList import LinkedList

class PersonaControl:
    def __init__(self):
        self.__persona = None
        self.__lista = LinkedList()

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
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self.__lista.add(self.__persona, self.__lista._length)
        
    def generate_id(self):
        return self.__lista._length + 1
    
    def guardar_crear_json(self,nombre ,data ):
        with open(f'{nombre}.json', 'w') as f: 
            json.dump(data, f)

