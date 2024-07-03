
from flask import Flask, Blueprint, url_for, jsonify, make_response, request, render_template, redirect, abort
from controller.personaDaoControl import PersonaDaoControl
from config.logging_config import log
import colorama
# from flask_cors import CORS

router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template('template.html', nombre='joe')

# Lista Personas
# @router.route('/personas/<tipo>/<attr>')
# def lista_persona(tipo, attr):
#     pd = PersonaDaoControl()
#     lista = pd._list()
#     lista.sort_models(attr, int(tipo))
#     return render_template('nene/lista.html', lista=pd.to_dic_lista(lista))

@router.route('/mapas')
def mapa():
    return render_template('d3/grafo.html')

# @router.route('/mapas_label')
# def mapa_label():
#     return render_template('d3/grafo_label.html')

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

