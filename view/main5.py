import sys

sys.path.append('../')
from math import nan
# from controller.tda.graph.graphManaged import GraphManaged
from controller.tda.graph.graphNoManaged import GraphNoManaged
# from controller.exception.arrayPositionException import ArrayPositionException

#? Pruebas de Graphos 

# ? Grafo Dirigido
if __name__ == "__main__":
    # try:
    #     graphoD = GraphManaged(5)
    #     graphoD.insert_edges(0, 4)
    # except Exception as error:
    #     print(error)
    # print(graphoD)
    

#? Grafo No Dirigido 
    try:
        grafo_no_dirigido = GraphNoManaged(12)
        # grafo_no_dirigido.insert_edges_weight(0, 4, 5)
        # grafo_no_dirigido.insert_edges_weight(1, 4, 15)
        grafo_no_dirigido.insert_edges(0, 4)
        grafo_no_dirigido.insert_edges(1, 3)
        grafo_no_dirigido.insert_edges(2, 3)
        grafo_no_dirigido.paint_graph()
    except Exception as e:
        print(e)
        