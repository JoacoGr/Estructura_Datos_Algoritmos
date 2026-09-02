import numpy as np
class cola:
    __dimension:int
    __lista: np.ndarray
    __inicio: int
    __ultimo: int
    __cant:int

    def __init__(self):
        self.__dimension = 5
        self.__lista= np.empty(self.__dimension, dtype='int')
        self.__inicio= 0
        self.__ultimo= 0
        self.__cant = 0

    def vacia(self):
        return (self.__cant == 0)

    def insertar(self, otro):
        if self.__cant < self.__dimension:
            self.__lista[self.__ultimo] = otro
            self.__ultimo=(self.__ultimo+1) % self.__dimension
            self.__cant += 1
            retorna = otro
        else: retorna = 0
        return retorna

    def suprimir(self):
        if(self.vacia()):
            print("Se encuentra vacia")
            retorna = 0
        else: 
            x = self.__lista[self.__inicio]
            self.__inicio = (self.__inicio+1) % self.__dimension
            self.__cant -= 1
            retorna = x
        return retorna

    def recorrer(self):
      if not self.vacia():
        i = self.__inicio
        for j in range(self.__cant):
          print(self.__lista[i])
          i = (i + 1) % self.__dimension


