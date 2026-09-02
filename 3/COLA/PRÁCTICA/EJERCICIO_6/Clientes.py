class cliente:
    __tiempo: int
    __espera: int
    __fin:bool

    def __init__(self, tiempo):
        self.__tiempo = tiempo
        self.__espera = 0
        self.__fin = False

    def get_tiempo(self):
        return self.__tiempo

    def get_espera(self):
        return self.__espera

    def set_tiempo(self):
        self.__tiempo -= 1

    def set_espera(self):
        self.__espera += 1

    def set_fin(self):
        self.__fin = True

    def get_fin(self):
        return self.__fin