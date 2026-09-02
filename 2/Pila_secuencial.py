import numpy as np
class pila:
    __cant: int
    __tope: int
    __pila: np.ndarray
    
    def __init__(self, cant):
        self.__cant = cant
        self.__tope = -1
        self.__pila = np.empty(self.__cant, dtype = int)
        
    def vacio(self):
        if self.__tope == -1:
            aux = True
        else: aux = False
        return aux
  
    def insertar(self, x):
        if self.__tope < self.__cant -1:
            self.__tope += 1
            self.__pila[self.__tope] = x
            aux = x
        else: aux = 0
        return aux
    
    def suprimir(self):
        if self.vacio():
            print("Pila vacia")
            aux = 0
        else: 
            aux = self.__pila[self.__tope]
            self.__tope -= 1
        return aux

    def mostrar(self):
        for i in range(self.__tope, -1 , -1):
            print(f'{self.__pila[i]}')
                
if __name__ == '__main__':
    pila1 = pila()
    if pila1.vacio():
        print("Está vacia")
    else: print("No está vacia")
    pila1.mostrar()
    print("-------------------")
    pila1.insertar(x = 46)
    pila1.insertar(x = 10)
    pila1.mostrar()
    print("-------------------")
    pila1.suprimir()
    pila1.mostrar()
    print("-------------------")
    pila1.suprimir()
    pila1.mostrar()
    if pila1.vacio():
        print("Está vacia")
    else: print("No está vacia")