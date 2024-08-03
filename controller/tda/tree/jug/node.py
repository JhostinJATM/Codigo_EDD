
from controller.tda.tree.jug.modelo.jug import Jug
from controller.tda.linked.linkedList import LinkedList

class Node():
    def __init__(self) -> None:
        self.__jD = Jug()
        self.__jD._capacity = 4
        self.__jD._current_capacity = 0
        self.__jL = Jug()
        self.__jL._capacity = 3
        self.__jL._current_capacity = 0
        self.__father = None
        self.__sucessors = LinkedList()

    @property
    def _jD(self):
        return self.__jD

    @_jD.setter
    def _jD(self, value):
        self.__jD = value

    @property
    def _jD(self):
        return self.__jD

    @_jD.setter
    def _jD(self, value):
        self.__jD = value

    @property
    def _jD(self):
        return self.__jD

    @_jD.setter
    def _jD(self, value):
        self.__jD = value

    @property
    def _jL(self):
        return self.__jL

    @_jL.setter
    def _jL(self, value):
        self.__jL = value

    @property
    def _jL(self):
        return self.__jL

    @_jL.setter
    def _jL(self, value):
        self.__jL = value

    @property
    def _jL(self):
        return self.__jL

    @_jL.setter
    def _jL(self, value):
        self.__jL = value

    @property
    def _father(self):
        return self.__father

    @_father.setter
    def _father(self, value):
        self.__father = value

    @property
    def _sucessors(self):
        return self.__sucessors

    @_sucessors.setter
    def _sucessors(self, value):
        self.__sucessors = value

    def set_current_capacity(self, ccjb, ccjl):
        self.__jD._current_capacity = ccjb
        self.__jL._current_capacity = ccjl
        # return True 

    def addSucessors(self, rules):
        self.__sucessors = LinkedList()
        print("Estoy con reglas")
        print(rules)
        for i in range(0, rules._length):
            aux = rules.get(i)
            aux._father = self 
            self.__sucessors.add(aux, self.__sucessors._length)

    def __str__(self) -> str:
        return f"{str(self.__jD)} : {str(self.__jL)}"