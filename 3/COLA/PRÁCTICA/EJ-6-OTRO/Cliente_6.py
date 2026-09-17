class cliente:
    __espera:int

    def __init__(self, tiempo):
        self.__tiempo = tiempo
        self.__espera = 0

    def get_tiempo(self):
        return self.__tiempo

    def set_tiempo(self):
        self.__tiempo -=1

    def get_espera(self):
        return self.__espera

    def set_espera(self):
        self.__espera += 1