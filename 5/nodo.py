class Nodo:
    __info: object
    __sig: object

    def __init__(self, info):
        self.__info = info
        self.__sig = None

    def get_sig(self):
        return self.__sig

    def get_info(self):
        return self.__info

    def set_sig(self, sig):
        self.__sig = sig