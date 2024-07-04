import sys

sys.path.append('../')
from math import nan
from controller.tda.graph.graphManaged import GraphManaged
from controller.tda.graph.graphNoManaged import GraphNoManaged
from controller.tda.graph.graphManagedLabel import GrafoDirigidoEtiquetado
from controller.exception.arrayPositionException import ArrayPositionException
from controller.tda.graph.graohLabelManaged import GraphLabelManaged
from controller.tda.graph.graphLabelNoManaged import GrafoEtiquetadoNoDirigido
from controller.personaControl import PersonaControl
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

    # objetos_array = [
    #     {'id': 1, 'nombre': 'Adelaide', 'apellido': 'Smith'},
    #     {'id': 2, 'nombre': 'Joel', 'apellido': 'Johnson'},
    #     {'id': 3, 'nombre': 'Lilith', 'apellido': 'Brown'},
    #     {'id': 4, 'nombre': 'Ennar', 'apellido': 'Taylor'}
    # ]

    # grafo_etiquetado = GrafoDirigidoEtiquetado(3, objetos_array)

    # #* AGREGAR ETIQUETAS
    # grafo_etiquetado.agregar_etiqueta(0, 1)
    # grafo_etiquetado.agregar_etiqueta(1, 2)
    # grafo_etiquetado.agregar_etiqueta(2, 3)
    # # grafo_etiquetado.imprimir_etiquetas()
    
    # #* PARA VERIFICAR SI UN VERTICE ESTA ETIQUETADO
    # # print(grafo_etiquetado.verificar_etiquetado(1))
    # # print(grafo_etiquetado.verificar_etiquetado(2))

    # #* PARA VERIFICAR SI TODOS VERTICES ESTAN ETIQUETADOS
    # # print(grafo_etiquetado.todos_etiquetados())

    # #* PARA OBTENER EL OBJETO DE UNA ETIQUETA
    # # print(grafo_etiquetado.obtener_objeto_etiqueta(1))
    
    # grafo_etiquetado.insertar_arista_peso(1, 2, 5)
    # grafo_etiquetado.insertar_arista_peso(0, 1, 4)
    # # grafo_etiquetado.paint_graph()

    # #*AGREGAR VERTICES
    # grafo_etiquetado.agregar_vertex()
    # grafo_etiquetado.agregar_etiqueta(3, 4)
    # grafo_etiquetado.agregar_vertex()
    # grafo_etiquetado.agregar_etiqueta(4, 3)
    
    # #* Obtener un vertice(objeto) por id 
    # print(f"Objeto del vertice 3: {grafo_etiquetado.obtener_obj(2)}")
    # print(f"Objeto del vertice 4: {grafo_etiquetado.obtener_obj(3)}")
    # grafo_etiquetado.paint_graph()
    
    
    # #! Grafo Etiquetado No Dirigido
    # graphD = GraphManaged(15)
    # graphL = GraphLabelManaged(15)
    
    # pc = PersonaControl()
    # pc._persona._apellido = "Leon" 
    # pc._persona._nombres = "Esteban"
    # graphL.label_vertex(1, pc._persona)
    # # graphL.label_vertex(pc._persona)
    # # print(pc._persona)
    # pc._persona = None
    # pc._persona._apellido = "Leon" 
    # pc._persona._nombres = "Esteban"
    # pc._persona._id = 2

    # graphL.label_vertex(0, 19)
    # graphL.label_vertex(1, 21)
    
    # print(graphL.getVertex(pc._persona))
    # graphL.paint_graph()
    # # print(graphL.getVertex(21))
    
    #! Grafo No Etiquetado No Dirigido
    
    graphL = GrafoEtiquetadoNoDirigido(5)
    

    graphL.label_vertex(0, 11)
    graphL.label_vertex(1, 12)
    graphL.label_vertex(2, 13)
    graphL.label_vertex(3, 14)
    graphL.label_vertex(4, 15)
    
    graphL.insertar_arista_peso_E(11, 12, 20)
    graphL.insertar_arista_peso_E(11, 13, 21)
    graphL.insertar_arista_peso_E(11, 14, 22)
    graphL.insertar_arista_peso_E(11, 15, 23)

    graphL.inserta_arista_E(12, 13)
    
    graphL.paint_graph()
    