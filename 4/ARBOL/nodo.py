class Nodo:
    __item:object
    __izq:Nodo
    __der:Nodo
    __cont:int

    def __init__(self):
        self.__item = None
        self.__izq = None
        self.__der = None
        self.__cont = 1

    def get_item(self):
        return self.__item

    def set_item(self, otro):
        self.__item = otro

    def set_izq(self, otro):
        self.__izq = otro

    def set_der(self, otro):
        self.__der = otro

    def get_izq(self):
        return self.__izq

    def get_der(self):
        return self.__der

    def incrementar_cont(self):
        self.__cont += 1

    def decrementar_cont(self):
        self.__cont -= 1

    def get_cont(self):
        return self.__cont
