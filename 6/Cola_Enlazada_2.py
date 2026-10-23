from Nodo_2 import nodo

class Cola:
    __cabeza: nodo
    __ultimo: nodo
    __cant: int

    def __init__(self):
        self.__cabeza = None
        self.__ultimo = None
        self.__cant = 0

    def vacio(self):
        return (self.__cant == 0)

    def insertar(self, x):
        nuevo_nodo = nodo(x)
        if self.vacio():
            self.__cabeza = nuevo_nodo
            self.__ultimo = nuevo_nodo
        else:
            self.__ultimo.set_sig(nuevo_nodo)
            self.__ultimo = nuevo_nodo
        self.__cant += 1
        return nuevo_nodo.get_vertice()

    def suprimir(self):
        if self.vacio():
            print("No hay elementos a eliminar")
            aux = None
        else:
            aux = self.__cabeza.get_vertice()
            self.__cabeza = self.__cabeza.get_sig()
            self.__cant -= 1
            if self.__cabeza is None:
                self.__ultimo = None
        return aux