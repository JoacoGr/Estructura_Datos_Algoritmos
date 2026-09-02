from Nodo import nodo

class cola:
    __inicio:nodo
    __ultimo:nodo
    __cant:int

    def __init__(self):
        self.__inicio = None
        self.__ultimo = None
        self.__cant = 0

    def vacio(self):
        return (self.__inicio == None)

    def insertar(self, otro):
        Nodo = nodo(otro)
        if self.__inicio == None:
            self.__inicio = Nodo
        else: 
            self.__ultimo.set_sig(Nodo)
        self.__ultimo = Nodo
        self.__cant += 1
        return self.__ultimo.get_item()

    def suprimir(self):
        if self.vacio():
            print("Cola vacia")
            retornar = None
        else:
            x = self.__inicio.get_item()
            self.__inicio = self.__inicio.get_sig()
            if self.__inicio == None:
                self.__ultimo = None
            self.__cant -= 1
            retornar = x
        return retornar

    def recorrer(self):
        aux = self.__inicio
        while aux is not None:
            print(aux)
            aux = aux.get_sig()

    def get_inicio(self):
        return self.__inicio