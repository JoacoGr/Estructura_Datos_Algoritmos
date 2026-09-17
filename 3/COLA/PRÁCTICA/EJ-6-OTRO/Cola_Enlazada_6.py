from Nodo_6 import nodo

class cola:
    __inicio:nodo
    __ultimo:nodo
    __cant: int

    def __init__(self):
        self.__inicio = None
        self.__ultimo = None
        self.__cant = 0

    def vacio(self):
        return (self.__cant == 0)

    def insertar(self, otro):
        Nodo = nodo(otro)
        if self.__inicio == None:
            self.__inicio = Nodo
        else:
            self.__ultimo.set_sig(Nodo)
        self.__ultimo = Nodo
        self.__cant += 1
        return otro

    def suprimir(self):
        if self.vacio():
            print("Error")
            eliminado = None
        else:
            eliminado = self.__inicio.get_item()
            self.__inicio = self.__inicio.get_sig()
            if self.__inicio == None:
                self.__ultimo = None
            self.__cant -= 1
        return eliminado

    def recorrer(self):
        aux = self.__inicio
        while aux is not None:
            print(aux.get_item())
            aux = aux.get_sig()

    def get_cant(self):
        return self.__cant

    def get_inicio(self):
        return self.__inicio