class trabajo:
    __tiempo: int
    __espera: int
    __finalizado = bool

    def __init__(self, tiempo):
        self.__tiempo = tiempo
        self.__espera = 0
        self.__finalizado = False

    def set_tiempo(self, tiempo):
        self.__tiempo -= tiempo

    def set_espera(self, espera):
        self.__espera += espera

    def get_tiempo(self):
        return self.__tiempo

    def get_espera(self):
        return self.__espera

    def get_finalizado(self):
        return self.__finalizado

    def set_finalizado(self):
        self.__finalizado = True