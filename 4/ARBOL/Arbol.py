from Raiz import raiz

class arbol:
    __raiz: raiz

    def __init__(self):
        self.__raiz = None

    def vacio(self):
        return (self.__raiz == None)

    def get_raiz(self):
        return self.__raiz

    def insertar(self, x):
        if self.vacio():
            
