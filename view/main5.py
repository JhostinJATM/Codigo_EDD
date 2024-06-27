import sys

sys.path.append('../')
from controller.tda.graph.graphManaged import GraphManaged
from controller.tda.graph.graphNoDirigido import GraphNoDirigido
from controller.exception.arrayPositionException import ArrayPositionException

#? Pruebas de Graphos 

# ? Grafo Dirigido
if __name__ == "__main__":
    # try:
    #     graphoD = GraphManaged(5)
    #     graphoD.insert_edges(0, 4)
    # except Exception as error:
    #     print(error)
    # print(graphoD)
    
    try:
        #? Creo un grafo no dirigido con 5 vértices
        graph = GraphNoDirigido(5)
        
        #? Se inserta algunas aristas con peso
        graph.insert_edges_weight(0, 1, 5)
        graph.insert_edges_weight(0, 2, 3)
        graph.insert_edges_weight(1, 3, 2)
        graph.insert_edges_weight(2, 4, 1)
        graph.insert_edges_weight(3, 4, 4)
        
        #? Imprimir el grafo, para verificar las aristas
        print("Estado del grafo no dirigido:")
        print(graph)
        
        #? Esto verificará si existen algunas aristas específicas
        print("¿Existe la arista entre el vértice 1 y el vértice 3?", graph.exist_edges(1, 3))
        print("¿Existe la arista entre el vértice 4 y el vértice 2?", graph.exist_edges(4, 2))
        
        #? Esto onsultara el peso de algunas aristas
        print("Peso de la arista entre el vértice 0 y el vértice 1:", graph.weight_edges(0, 1))
        print("Peso de la arista entre el vértice 3 y el vértice 4:", graph.weight_edges(3, 4))
        
    except ArrayPositionException as e:
        print(f"Error: {e}")