class nodo:
    __item:object
    __sig:None

    def __init__(self, otro):
        self.__item = otro
        self.__sig = None

    def get_item(self):
        return self.__item

    def get_sig(self):
        return self.__sig

    def set_sig(self, sig):
        self.__sig = sig
        