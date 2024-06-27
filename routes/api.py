from flask import Flask, Blueprint, jsonify, make_response, request
from controller.personaDaoControl import PersonaDaoControl
api = Blueprint('api', __name__)
from flask_cors import CORS

#GET es para representar datos
#POST guardar datos, modificar datos y el inicio de sesion

CORS(api)
cors = CORS(api, resource={
    r"/*":{
        "origins":"*"
    }
})


@api.route('/')
def home():
    return make_response(
        jsonify({"msg":"OK", "code": 200}),
        200
    )

#* Lista Personas
@api.route('/api/personas')
def lista_persona():
    pd = PersonaDaoControl()
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": pd.to_dict()}),
        200
    )
    
# #* Guaradar personas
@api.route('/api/personas/guardar', methods=["POST"])
def guardar_persona():
    pd = PersonaDaoControl()
    data = request.json
    print(type(data))
    if not "apellido" in data.keys():
        return make_response(
            jsonify({"msg":"Faltan datos", "code": 4000, "data": []}),
            400
        )
    #TODO ...Validar 
    pd._persona._apellido = data['apellido']
    pd._persona._nombres = data['nombres']
    pd._persona._direccion = data['direccion']
    pd._persona._dni = data['dni']
    pd._persona._telefono = data['telefono']
    pd.save
    return make_response(
        jsonify({"msg":"OK, se ah registrado correctamente", "code": 200, "data": []}),
        200
    )
