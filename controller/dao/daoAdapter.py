from typing import TypeVar, Generic, Type
import logging as log
from controller.tda.linked.linkedList import LinkedList
import os.path
from numbers import Number
from controller.connection.conecction import Connection
import json
import os 
import enum 
import colorama

T = TypeVar("T")
class DaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T):
        self.atype = atype
        self.__name = atype.__name__.lower()
        conexion = Connection()
        self.conn = conexion.connection("root", '2002', "estructura2024", '127.0.0.1')

    def _list(self) -> T:
        lista = LinkedList()
        cur = self.conn._db.cursor()
        cur.execute(f"SELECT * FROM {self.__name}")
        for row in cur.fetchall():
            a = self.atype.deserializar(row)
            lista.add(a, lista._length)
        return lista
        
    def _get(self, id):
        lista = self._list() 
        array = lista.toArray
        for i in range (0, len(array)):
            if array[i]._id == id:
                return array[i]
        return None
    
    def _save(self, data: T) -> T:
        aux = data.serializable
        # print(aux)
        columns = ""
        for cont in aux:
            # print(len(str(aux[cont])))
            if len(str(aux[cont])) > 0:
                columns += cont + ","
        columns = columns.rstrip(columns[-1])
        sql = "Insert into "+self.__name+" ("+columns+") value("
        data = ""
        for cont in aux:
            if len(str(aux[cont])) > 0:
                if isinstance(aux[cont], Number) or isinstance(aux[cont], bool):
                    # print(type(aux[cont]))
                    data += str(aux[cont]) + ","
                elif isinstance(aux[cont], enum.Enum):
                    data += '"' + aux[cont].getValue()+ '"' + + ","
                else:
                    # print(type(aux[cont]))
                    data += '"' + aux[cont]+ '"' +","
        data = data.rstrip(data[-1])
        sql = "Insert into "+self.__name+" ("+columns+") value("+data+")"
        cur = self.conn._db.cursor()
        print(colorama.Fore.RED + f"Log: {sql}" + colorama.Fore.RESET)
        cur.execute(sql)
        self.conn._db.commit()
        print('HoLA')
        # print(id)
   
    def to_dic_lista(self, lista):
        aux = []
        arreglo = lista.toArray
        for i in range(0, lista._length):
            aux.append(arreglo[i].serializable)
        return aux
   
    def _merge(self, data: T, pos) -> T:
        try:
            self._list()
            self.lista.edit(data, pos)
            a = open(self.URL+self.file, "w")
            a.write(self.__tranform__())
            a.close()
        except Exception as e:
            log.debug(f"Error en merge es: {e}")

    def to_dict(self):
        aux = []
        lista =self._list()
        for i in range(0, lista._length):
            # aux.append(lista.get(i).serializable)
            aux.append(aux[i].serializable)
        return aux

    def __tranform__(self):
        try:
            aux = "["
            for i in range(0, self.lista._length):
                if i < self.lista._length - 1:
                    aux += str(json.dumps(self.lista.get(i).serializable))+","
                else:
                    aux += str(json.dumps(self.lista.get(i).serializable))
            aux += "]"
            return aux
        except Exception as e:
                print(f"Error en transform es: {e}")
                
