from Nodo_2 import nodo
class cola:
    __inicio:nodo
    __ultimo:nodo
    __cant:int

    def __init__(self):
        self.__cabeza = None
        self.__ultimo = None
        self.__cant = 0

    def vacio(self):
        return (self.__cant == 0)

    def insertar(self, x):
        Nodo = nodo(x)
        if self.__vacio():
            self.__cabeza = Nodo
        else:
            self.__ultimo.set_sig(Nodo)
        self.__cant += 1
        return self.__ultimo.get_sig()

    def suprimir(self):
        if self.vacio():
            print("No hay elementos a eliminar")
            aux = None
        else:
            aux = self.__cabeza.get_item()
            self.__cabeza = self.__cabeza.get_sig()
            self.__cant -= 1
            if self.__cabeza == None:
                self.__ultimo = None
        return aux
            