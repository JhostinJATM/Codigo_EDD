
import sys

sys.path.append('../')
from controller.personaDaoControl import PersonaDaoControl
import random
import time
from controller.tda.linked.linkedList import LinkedList
from controller.connection.conecction import Connection


if __name__ == "__main__":
    pdc = PersonaDaoControl()
    try:
        # connection = Connection()
        # connection.connection("root", '2002', "estructura2024", '127.0.0.1')
        # if connection._db:
        #     print("conectado")
        # pdc._persona._apellido = 'Demmer'
        # pdc._persona._nombres = 'Eulis'
        # pdc.save
        # pdc._persona = None
        lista = pdc._list()
        lista.print
        print(pdc._get(2))
        # lista.sort_models("_nombres", 1)
        # lista.print
    except Exception as e:
        print(e)