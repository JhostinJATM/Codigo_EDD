import sys
import os
import colorama 

sys.path.append('../')
from controller.tda.queque.quequeOperation import QuequeOperation
from controller.tda.stack.stackOperation import StackOperation
from controller.censoDao import CensoDao 
from controller.personaDaoControl import PersonaDaoControl


from controller.calculos import Calculos
from controller.tdaArray import TDAArray
from model.persona import Persona
from controller.tda.linked.linkedList import LinkedList
from controller.personaControl import PersonaControl
import random
import time
import string

colorama.init()

def limpira_consola():
    os.system('cls||cls||clear')

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

if __name__ == "__main__":
    try:
        lista = LinkedList()
        
        # for i in range(500):
            # lista.add(random.randint(0, 1000))

        for i in range(50):
            lista.add(generate_random_string(random.randint(5, 10)))

            # lista.add(round(random.random()*1000, 2))
        # lista.print
        # arreglo = lista.toArray
        # print(arreglo)
        # lista.toList(arreglo)
        # lista.print
        inicio = time.time()
        # lista.sort(1)
        # arreglo = lista.toArray
        lista_ordenada = lista.tim_sort(lista.toArray)
        # print(lista_ordenada)
        fin = time.time()
        print(f"El tiempo de ejecucion es: {fin - inicio}")
        

    except Exception as e:
        print(f"El error es: {e}")
        
        
colorama.deinit()