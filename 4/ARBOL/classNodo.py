class nodo:
    __clave: int
    __cont: int
    __izq: object
    __der: object

    def __init__(self, clave):
        self.__clave = clave
        self.__izq = None
        self.__der = None
        self.__cont = 0

    def getClave(self):
        return self.__clave
    def setClave(self, clave):
        self.__clave = clave

    def setIzq(self,izqC):
        self.__izq = izqC

    def getIzq(self):
        return self.__izq

    def setDer(self,derC):
        self.__der = derC

    def getDer(self):
        return self.__der

    def getCont(self):
        return self.__cont

    def setCont(self, contC):
        self.__cont = contC

    def incrementarCont(self, num):
        self.__cont += num