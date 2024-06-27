from controller.tda.graph.graph import Graph
from controller.tda.linked.linkedList import LinkedList
from controller.exception.arrayPositionException import ArrayPositionException
from controller.tda.graph.adjacent import Adjacent
from math import nan

class GraphNoDirigido(Graph):
    def __init__(self, num_vert) -> None:
        super().__init__()
        self.__numVert = num_vert
        self.__numEdg = 0
        self.__listAdjacent = []
        for i in range(0, num_vert):
            self.__listAdjacent.append(LinkedList())
    
    @property
    def num_vertex(self):
        return self.__numVert

    @property
    def num_edges(self):
        return self.__numEdg

    def exist_edges(self, v1, v2):
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            return self.__exist_edges_helper(v1, v2) or self.__exist_edges_helper(v2, v1)
        else:
            raise ArrayPositionException("Delimite out")

    def __exist_edges_helper(self, v1, v2):
        listAdj = self.__listAdjacent[v1]
        if not listAdj.isEmpty:
            arrayAdj = listAdj.toArray
            for i in range(0, listAdj._length):
                adj = arrayAdj[i]
                if adj._destination == v2:
                    return True
        return False
    
    def weight_edges(self, v1, v2):
        if self.exist_edges(v1, v2):
            listAdj = self.__listAdjacent[v1]
            if not listAdj.isEmpty:
                arrayAdj = listAdj.toArray
                for i in range (0, listAdj._length):
                    adj = arrayAdj[i]
                    if adj._destination == v2:
                        return adj._weight
        else:
            raise ArrayPositionException("Delimite out")
    
    def insert_edges_weight(self, v1, v2, weight):
        if v1 <= self.num_vertex and v2 <= self.num_vertex:
            if not self.__exist_edges_helper(v1, v2):
                self.__numEdg += 1
                adj = Adjacent()
                adj._destination = v2
                adj._weight = weight
                self.__listAdjacent[v1].add(adj, self.__listAdjacent[v1]._length)
                # Para asegurar la bidireccionalidad en el grafo no dirigido
                self.__listAdjacent[v2].add(adj, self.__listAdjacent[v2]._length)
        else:
            raise ArrayPositionException("Delimite out")
       
    def insert_edges(self, v1, v2):
        self.insert_edges_weight(v1, v2, nan)
        
    def adjacent(self, v1):
        return self.__listAdjacent[v1]
