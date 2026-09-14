import numpy as np
class pila:
    __tope:int
    __cant:int
    __pila: np.ndarray

    def __init__(self):
        self.__cant = 3
        self.__tope = -1
        self.__pila = np.empty(self.__cant, dtype=object)

    def vacio(self):
        return (self.__tope == -1)
    
    def insertar(self, x):
        if self.__tope < self.__cant -1:
            self.__tope += 1
            self.__pila[self.__tope] = x
            aux = x
        else:
            print("No hay espacio suficiente")
            aux = None
        return aux

    def suprimir(self):
        if not self.vacio():
            aux = self.__pila[self.__tope]
            self.__tope-=1
        else:
            print("No hay elementos a eliminar")
            aux = None
        return aux

    def recorrer(self):
        for i in range(self.__tope, -1, -1):
            print(self.__pila[i])

if __name__ == '__main__':
    pila1 = pila()
    pila1.insertar(1)
    pila1.insertar(2)
    pila1.insertar(3)
    pila1.insertar(4)
    pila1.recorrer()
    print("-------------------------")
    pila1.suprimir()
    pila1.recorrer()
    print("----------------")
    pila1.suprimir()
    pila1.suprimir()
    pila1.suprimir()
    pila1.recorrer()
