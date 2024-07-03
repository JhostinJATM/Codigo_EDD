import sys

sys.path.append('../')
from math import nan
# from controller.tda.graph.graphManaged import GraphManaged
from controller.tda.graph.graphNoManaged import GraphNoManaged
from controller.tda.graph.graphManagedLabel import GrafoDirigidoEtiquetado
# from controller.exception.arrayPositionException import ArrayPositionException

#? Pruebas de Graphos 

# ? Grafo Dirigidoz
if __name__ == "__main__":
    # try:
    #     graphoD = GraphManaged(5)
    #     graphoD.insert_edges(0, 4)
    # except Exception as error:
    #     print(error)
    # print(graphoD)
    

# #? Grafo No Dirigido 
#     try:
#         grafo_no_dirigido = GraphNoManaged(12)
#         # grafo_no_dirigido.insert_edges_weight(0, 4, 5)
#         # grafo_no_dirigido.insert_edges_weight(1, 4, 15)
#         grafo_no_dirigido.insert_edges(0, 4)
#         grafo_no_dirigido.insert_edges(1, 3)
#         grafo_no_dirigido.insert_edges(2, 3)
#         grafo_no_dirigido.paint_graph()
#     except Exception as e:
#         print(e)
        
        
        
    #! TAREA GRAGO DIRIGIDO ETIQUETADO

    objetos_array = [
        {'id': 1, 'nombre': 'Adelaide', 'apellido': 'Smith'},
        {'id': 2, 'nombre': 'Joel', 'apellido': 'Johnson'},
        {'id': 3, 'nombre': 'Lilith', 'apellido': 'Brown'},
        {'id': 4, 'nombre': 'Ennar', 'apellido': 'Taylor'}
    ]

    grafo_etiquetado = GrafoDirigidoEtiquetado(3, objetos_array)

    #* AGREGAR ETIQUETAS
    grafo_etiquetado.agregar_etiqueta(0, 1)
    grafo_etiquetado.agregar_etiqueta(1, 2)
    grafo_etiquetado.agregar_etiqueta(2, 3)
    # grafo_etiquetado.imprimir_etiquetas()
    
    #* PARA VERIFICAR SI UN VERTICE ESTA ETIQUETADO
    # print(grafo_etiquetado.verificar_etiquetado(1))
    # print(grafo_etiquetado.verificar_etiquetado(2))

    #* PARA VERIFICAR SI TODOS VERTICES ESTAN ETIQUETADOS
    # print(grafo_etiquetado.todos_etiquetados())

    #* PARA OBTENER EL OBJETO DE UNA ETIQUETA
    # print(grafo_etiquetado.obtener_objeto_etiqueta(1))
    
    grafo_etiquetado.insertar_arista_peso(1, 2, 5)
    grafo_etiquetado.insertar_arista_peso(0, 1, 4)
    # grafo_etiquetado.paint_graph()

    #*AGREGAR VERTICES
    grafo_etiquetado.agregar_vertex()
    grafo_etiquetado.agregar_etiqueta(3, 4)
    grafo_etiquetado.agregar_vertex()
    grafo_etiquetado.agregar_etiqueta(4, 3)
    
    #* Obtener un vertice(objeto) por id 
    print(f"Objeto del vertice 3: {grafo_etiquetado.obtener_obj(2)}")
    print(f"Objeto del vertice 4: {grafo_etiquetado.obtener_obj(3)}")
    grafo_etiquetado.paint_graph()