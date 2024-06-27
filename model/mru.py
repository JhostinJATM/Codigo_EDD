class MRU:
    def __init__(self) -> None:
        self.__distancia = 0.0
        self.__velocidad = 0.0
        self.__tiempo = 0.0

    @property
    def _distancia(self):
        return self.__distancia

    @_distancia.setter
    def _distancia(self, value):
        self.__distancia = value

    @property
    def _velocidad(self):
        return self.__velocidad

    @_velocidad.setter
    def _velocidad(self, value):
        self.__velocidad = value

    @property
    def _tiempo(self):
        return self.__tiempo

    @_tiempo.setter
    def _tiempo(self, value):
        self.__tiempo = value

    def __str__(self) -> str:
        return "v = " + str(self._velocidad) + " " + str(self._tiempo) + " x " + str(self._distancia)
