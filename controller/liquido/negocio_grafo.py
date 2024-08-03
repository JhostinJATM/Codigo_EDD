from controller.liquido.negocioDaoControl import NegocioControl
from controller.tda.graph.graphLabelNoManaged import GraphLabelNoManaged
import os
import json

class NegocioGrafo:
    def __init__(self):
        self.__grafo = None
        self._nado = NegocioControl()
        
    def create_graph(self, data):
        print(json)
        list = self._nado._list()
        if list._length > 0:
            self.__grafo = GraphLabelNoManaged(list._length)
            arr = list.toArray
            for i in range(0, len(arr)):
                self.__grafo.label_vertex(i, arr[i])
            self.__grafo.paint_graph(data)
            
   