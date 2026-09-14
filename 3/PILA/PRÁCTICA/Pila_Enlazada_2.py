from Nodo_2 import nodo
class pila:
    __cabeza: nodo
    __cant:int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0

    def vacio(self):
        return (self.__cant == 0)

    def insertar(self, x):
        Nodo = nodo(x)
        Nodo.set_sig(self.__cabeza)
        self.__cabeza = Nodo
        self.__cant += 1

    def suprimir(self):
        if self.vacio():
            print("No hay elementos a eliminar")
            aux = None
        else:
            aux = self.__cabeza.get_item()
            self.__cabeza = self.__cabeza.get_sig()
            self.__cant -= 1
        return aux

    def recorrer(self):
        aux = self.__cabeza
        while aux is not None:
            print(aux.get_item())
            aux = aux.get_sig()

    