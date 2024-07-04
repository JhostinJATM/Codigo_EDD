from controller.tda.graph.graohLabelManaged import GraphLabelManaged
from controller.exception.arrayPositionException import ArrayPositionException
from math import nan

class GrafoEtiquetadoNoDirigido(GraphLabelManaged):
    def __init__(self, num_vert):
        super().__init__(num_vert)
        
    def inserta_arista_E(self, label1, label2):
        self.insertar_arista_peso_E(label1, label2, nan)
        
    def insertar_arista_peso_E(self, label1, label2, weight):
        v1 = self.getVertex(label1)
        v2 = self.getVertex(label2)
        if v1 != -1 and v2 != -1:
            self.insert_edges_weight(v1, v2, weight)
            self.insert_edges_weight(v2, v1, weight) 
        else:
            raise ArrayPositionException("Delimite out")
        
