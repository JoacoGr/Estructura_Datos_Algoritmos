class trabajo:
    __tiempo: int
    __espera: int
    __finalizado: bool

    def __init__(self, tiempo):
        self.__tiempo = tiempo
        self.__espera = 0
        self.__finalizado = False

    def get_tiempo(self):
        return int(self.__tiempo)

    def get_espera(self):
        return int(self.__espera)

    def get_finalizado(self):
        return self.__finalizado

    def set_finalizado(self, otro):
        self.__finalizado = otro

    def set_espera(self, otro):
        self.__espera += otro

    def set_tiempo(self, otro):
        self.__tiempo -= otro