from model.enumTipoIdentificacion import EnumTipoIdentificacion

class Persona:
    def __init__(self):
        self.__id = 0
        self.__apellido = ""
        self.__nombres = ""
        self.__dni = ""
        self.__direccion = ""
        self.__telefono = ""
        # self.__tipoidentificacion = ""
        self.__tipoidentificacion = EnumTipoIdentificacion.CEDULA

    @property
    def _tipoidentificacion(self):
        return self.__tipoidentificacion

    @_tipoidentificacion.setter
    def _tipoidentificacion(self, value):
        self.__tipoidentificacion = value

    # @property
    # def _tipoidentificacion(self):
    #     return self.__tipoidentificacion

    # @_tipoidentificacion.setter
    # def _tipoidentificacion(self, value):
    #     self.__tipoidentificacion = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _nombres(self):
        return self.__nombres

    @_nombres.setter
    def _nombres(self, value):
        self.__nombres = value

    @property
    def _dni(self):
        return self.__dni

    @_dni.setter
    def _dni(self, value):
        self.__dni = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    @property
    def serializable(self):
        return {
            "id": self.__id,
            "apellido": self.__apellido ,
            "nombres": self.__nombres ,
            "telefono": self.__telefono ,
            "dni": self.__dni ,
            "direccion": self.__direccion ,
            # "tipoidentificacion": self.__tipoidentificacion
            "tipoidentificacion": self._tipoidentificacion.getValue()
        }

    def deserializar(data):
        persona = Persona()
        persona._id = data["id"]
        persona._apellido = data["apellido"]
        persona._nombres = data["nombres"]
        persona._telefono = data["telefono"]
        persona._dni = data["dni"]
        persona._direccion = data["direccion"]
        # persona._tipoidentificacion = data["tipoidentificacion"]
        persona._tipoidentificacion = EnumTipoIdentificacion[data["tipoidentificacion"]]
        return persona

    def __str__(self) -> str:
        return f"{self.__apellido} {self.__nombres}"
    
    
    