
import sys

sys.path.append('../')
from controller.personaDaoControl import PersonaDaoControl
import random
import time
from controller.tda.linked.linkedList import LinkedList


if __name__ == "__main__":
    pcd = PersonaDaoControl()
    lista = LinkedList()
    for i in range(5):
        lista.add(round(random.random()*100,2))
    lista.add(32.5)
    # lista.print
    inicio = time.time()
    lista.sort(2)
    fin = time.time()
    # print(f"El tiempo de ejecucion es: {fin - inicio}") 
    # lista.print
    listaS = LinkedList()
    listaS.add("Edith Lincon", listaS._length)
    listaS.add("Lilith Brinston", listaS._length)
    listaS.add("Edher Esquivel", listaS._length)
    listaS.add("Summer Hernandez", listaS._length)
    listaS.add("Immirael Hernandez", listaS._length)
    listaS.add("Ennar Martinez", listaS._length)
    listaS.add("Lelith Brinston", listaS._length)
    listaS.add("Lummer Constan", listaS._length)
    listaS.add("Dante Vorns", listaS._length)
    listaS.add("Leonidas Sparda", listaS._length)
    # listaS.print
    listaS.sort(1)
    # listaS.print
    # pcd._list().print
    lista_aux = pcd._list().sort_models("_apellido", 1)
    lista_aux.print
    
    # print(f"Hola Buscado")
    # listita = listaS.search_equals('Dante')
    # listita.print
    # print("Edith".lower().__eq__("Edith"))