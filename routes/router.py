
from flask import Flask, Blueprint, url_for, jsonify, make_response, request, render_template, redirect, abort
from controller.personaDaoControl import PersonaDaoControl
from controller.liquido.negocioDaoControl import NegocioControl
from controller.liquido.negocio_grafo import NegocioGrafo
from controller.tda.graph.Utilidades import haversine
import colorama
import numpy as np
import os 
import json
# from flask_cors import CORS

router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template('template.html', nombre='joe')

@router.route('/negocios/guardar_json', methods=['POST'])
def guardar_matriz_json():
    try:
        data = request.get_json()
        ruta_actual = os.path.dirname(__file__)
        ng = NegocioGrafo()
        ng.create_graph(data)
        with open(os.path.join(ruta_actual, 'grafo.json'), 'w') as f:
            json.dump(data, f)
        return jsonify({"message": "Guardado en JSON exitosamente."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@router.route('/negocios/cargar_json', methods=['GET'])
def cargar_matriz_json():
    try:
        ruta_actual = os.path.dirname(__file__)
        with open(os.path.join(ruta_actual, 'grafo.json')) as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "El archivo grafo.json no existe."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@router.route('/negocios')
def lista_negocios():
    pd = NegocioControl()
    lista = pd._list()
    lista.sort_models("_id")
    return render_template('liquido/lista.html', lista=pd.to_dic_lista(lista))

@router.route("/negocios/agregar")
def agregar_negocio():
    return render_template('liquido/guardar.html')

@router.route("/negocios/guardar_distancia/<int:origen>/<int:destino>", methods=['POST'])
def agregar_distancia(origen, destino):
    try:
        pd = NegocioControl()
        lista = pd._list().quick_models("_id")
        inicio = lista.busqueda_binaria("_id", origen)
        final = lista.busqueda_binaria("_id", destino)
        distancia = round(float(haversine(np.array([inicio._lng]), np.array([inicio._lat]), np.array([final._lng]), np.array([final._lat]))), 4)
        return jsonify({"distancia": distancia, "message": "Distancia guardada exitosamente."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@router.route('/negocios/guardar', methods = ['POST'])  
def guardar_negocio():
    print("\n\n\n\n\n")
    pd = NegocioControl()
    data = request.form
    print(data)
    if not "nombre" in data.keys() or not "direccion" in data.keys() or not "horario" in data.keys() or not "latitud" in data.keys() or not "longitud" in data.keys():
       abort(400)
    #TODO ...Validar 
    pd._negocio._nombre = data['nombre']
    pd._negocio._direccion = data['direccion']
    pd._negocio._horario = data['horario']
    pd._negocio._lat = request.form['latitud']
    pd._negocio._lng = request.form['longitud']
    pd.save
    print("\n\n\n\n\n")
    return redirect("/negocios", code=302)

#* Grafo
@router.route('/grafo')
def grafo():
    return render_template('d3/grafo.html')

@router.route('/negocios/grafo_negocio')
def grafo_negocio():
    ng = NegocioGrafo()
    ng.create_graph()
    return render_template('d3/grafo.html')

@router.route('/negocios/grafo_ver_admin')
def grafo_ver_admin():
    pd = NegocioControl()
    lista = pd._list()
    if not lista.isEmpty:
        # lista.sort_models("_nombre", 2)
        lista.sort_models("_id")
    return render_template('liquido/grafo.html', lista=pd.to_dic_lista(lista))

#* Personas
# Lista Personas
# @router.route('/personas/<tipo>/<attr>')
# def lista_persona(tipo, attr):
#     pd = PersonaDaoControl()
#     lista = pd._list()
#     lista.sort_models(attr, int(tipo))
#     return render_template('nene/lista.html', lista=pd.to_dic_lista(lista))


@router.route('/personas')
def lista_persona():
    pd = PersonaDaoControl()
    lista = pd._list()
    lista.sort_models("_apellido", 1)
    return render_template('nene/lista.html', lista=pd.to_dic_lista(lista))

@router.route('/personas/<tipo>/<attr>')
def lista_personas_ordenar(tipo, attr):
    pd = PersonaDaoControl()
    lista = pd._list()
    lista.sort_models(attr, int(tipo))
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": pd.to_dic_lista(lista)}),
        200
    )

#!-----------------------EDITAR--------------------------
@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._get(int(pos))#pd._list().get(int(pos) - 1)
    print(nene)
    return render_template('nene/editar.html', data=nene)

@router.route('/personas/ver')
def ver_guardar():
    return render_template('nene/guardar.html')


@router.route('/personas/guardar', methods = ['POST'])  
def guardar_persona():
    pd = PersonaDaoControl()
    data = request.form
    # print(data)
    # print(type(data))
    if not "apellido" in data.keys():
       abort(400)
    #TODO ...Validar 
    pd._persona._apellido = data['apellido']
    pd._persona._nombres = data['nombres']
    pd._persona._direccion = data['direccion']
    pd._persona._dni = data['dni']
    pd._persona._telefono = data['telefono']
    pd.save
    return redirect("/personas", code=302)


@router.route('/personas/modificar', methods = ['POST'])  
def modifcar_personas():
    # try:
    pd = PersonaDaoControl()
    data = request.form
    print("------------------------------------")
    print(colorama.Fore.GREEN +f'id pasado desde el formulario: {data["id"]} -- {type(data["id"])}')
    print("------------------------------------")
    pos_int = int(data["id"])
    print(colorama.Fore.BLUE +f'id transformado: {pos_int} -- {type(pos_int)}')
    nene = pd._list().get(pos_int - 1)
    if not "apellido" in data.keys():
        abort(400)
    #TODO ...Validar 
    pd._persona = nene
    pd._persona._apellido = data['apellido']
    pd._persona._nombres = data['nombres']
    pd._persona._direccion = data['direccion']
    pd._persona._dni = data['dni']
    pd._persona._telefono = data['telefono']
    pd.merge(pos_int - 1)
    return redirect("/personas", code=302)
    # except Exception as e:
    #     log.error(e)

