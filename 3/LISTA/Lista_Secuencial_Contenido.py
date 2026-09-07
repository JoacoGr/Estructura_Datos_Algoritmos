import numpy as np
class lista:
    __dimension: int
    __cantidad: int
    __lista: np.ndarray

    def __init__(self):
        self.__dimension = 10
        self.__cantidad = 0
        self.__lista = np.empty(self.__dimension, dtype="int")

    def vacio(self):
        return (self.__cantidad == 0)

    def insertar(self, otro):
        if self.__dimension == self.__cantidad:
            print("Error de espacio")
            return
        i = 0
        while i < self.__cantidad and self.__lista[i] < otro:
                i += 1

        j = self.__cantidad
        while j > i:
            self.__lista[j] = self.__lista[j-1]
            j -= 1
        self.__lista[i] = otro
        self.__cantidad += 1

    def suprimir(self, otro):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__lista[i] == otro:
                encontrado = True
            else: i+=1 
        if encontrado:
            while i < self.__cantidad:
                self.__lista[i] = self.__lista[i+1]
                i +=1
            self.__cantidad -= 1
        else: print("No se halló")

    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__lista[i])

    def buscar(self, otro):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__lista[i] == otro:
                encontrado = True
            else:
                i+=1
        if not encontrado:
            print("No se halló")
            return -1
        return i
            


if __name__ == '__main__':
    li = lista()
    li.insertar(1)
    li.insertar(2)
    li.insertar(3)
    li.insertar(6)
    li.insertar(4)
    li.mostrar()
    print("-------------")
    li.suprimir(3)
    li.mostrar()
    print("---------")
    print(li.buscar(2))