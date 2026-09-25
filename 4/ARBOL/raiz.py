class raiz:
    __item:object
    __izq:raiz
    __der:raiz

    def __init__(self, otro):
        self.__item = otro
        self.__izq = None
        self.__der = None

    def get_item(self):
        return self.__item

    def set_izq(self, otro):
        self.__izq = otro

    def set_der(self, otro):
        self.__der = otro

    def get_izq(self):
        return self.__izq

    def get_der(self):
        return self.__der
