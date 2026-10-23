class nodo:
    __vertice:object
    __sig:None

    def __init__(self, otro):
        self.__vertice = otro
        self.__sig = None

    def get_vertice(self):
        return self.__vertice

    def get_sig(self):
        return self.__sig

    def set_sig(self, sig):
        self.__sig = sig
        