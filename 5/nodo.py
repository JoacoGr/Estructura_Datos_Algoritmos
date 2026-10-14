class Nodo:
    __clave: object
    __sig: object

    def __init__(self, info):
        self.__clave = info
        self.__sig = None

    def get_sig(self):
        return self.__sig

    def get_clave(self):
        return self.__clave

    def set_sig(self, sig):
        self.__sig = sig