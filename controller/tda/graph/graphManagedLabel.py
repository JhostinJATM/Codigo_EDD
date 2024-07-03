import os
from controller.tda.graph.graphManaged import GraphManaged
from controller.exception.arrayPositionException import ArrayPositionException
from controller.tda.linked.linkedList import LinkedList

class GrafoDirigidoEtiquetado(GraphManaged):
    def __init__(self, num_vertices, array_objs):
        super().__init__(num_vertices)
        self.etiquetas = [None] * num_vertices
        self.array_objs = array_objs
    
    def agregar_etiqueta(self, vertex, id):
        obj = next((item for item in self.array_objs if item['id'] == id), None)
        if obj is not None:
            self.etiquetas[vertex] = obj
        else:
            raise ArrayPositionException("ID no encontrado en array_objs")

    def insertar_arista_peso(self, obj1, obj2, weight):
        if self.all_etiquetados():
            self.insert_edges_weight(obj1, obj2, weight)
        else:
            raise ArrayPositionException("No todos los vértices están etiquetados")

    def verify_vertex_etiquetado(self, vertex):
        return self.etiquetas[vertex] is not None

    def all_etiquetados(self):
        return all(etiqueta is not None for etiqueta in self.etiquetas)
    
    def obtener_obj(self, id):
        return self.etiquetas[id]
        
    def agregar_vertex(self):
        # print(f"Numero de vertices: {self.num_vertex}")
        # nuevo_numero = self.num_vertex + 1
        # print(f"Nuevo numero: {nuevo_numero}")
        # self.setNumVertex(nuevo_numero)
        # print(f"Numero de vertices: {self.num_vertex}")
        self.setNumVertex(self.num_vertex + 1)
        self._listAdjacent.append(LinkedList())
        self.etiquetas.append(None)
        
    def egde_existe(self, obj1, obj2):
        return self.exist_edges(obj1, obj2)
    
    def peso_entre_arista(self, obj1, obj2):
        return self.weight_edges(obj1, obj2)
    
    #* METODOS DE PRUEBA
    
    def imprimir_array_objs(self):
        print(f"ARRAY_OBJS: \n{self.array_objs}\n")

    def imprimir_longitud_array_objs(self):
        print(f"Longitud ARRAY_OBJS: \n{len(self.array_objs)}\n")

    def imprimir_etiquetas(self):
        print(f"Imprimiendo etiquetas: \n{self.etiquetas}\n")

    def imprimir_longitud_etiquetas(self):
        print(f"Longitud de etiquetas: \n{len(self.etiquetas)}\n")
            
    def paint_graph(self):
        if self.all_etiquetados():
            url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"/static/d3/grafo.js"
            js = 'var nodes = new vis.DataSet(['
            for i, obj in enumerate(self.etiquetas):
                if obj:
                    js += '{id: ' + str(i + 1) + ',label:"' + obj["nombre"] + ' ' + obj["apellido"] + '"},' + '\n'
            js += ']);\n'

            js += 'var edges = new vis.DataSet(['
            for i in range(self.num_vertex):
                adjs = self.adjacent(i)
                if not adjs.isEmpty:
                    for j in range(adjs._length):
                        adj = adjs.get(j)
                        js += '{from:' + str(i + 1) + ',to:' + str(adj._destination + 1) + ', label:"' + str(adj._weight) + '"},' + "\n"
            js += ']);\n'
            js += "var container = document.getElementById('mynetwork'); var data = {nodes: nodes, edges: edges}; var options = {}; var network = new vis.Network(container, data, options);"

            with open(url, 'w') as file:
                file.write(js)
        else:
            raise ArrayPositionException("No todos los vértices están etiquetados")
            