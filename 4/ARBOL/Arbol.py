from nodo import Nodo

class arbol:
    __raiz: Nodo

    def __init__(self):
        self.__raiz = None

    def vacio(self):
        return (self.__raiz == None)

    def get_raiz(self):
        return self.__raiz
        
    def insertarraiz(self, x):
        aux = Nodo()
        aux.set_item(x)
        aux.set_izq(None)
        aux.set_der(None)
        self.__raiz = aux

    def get_raiz(self):
        return self.__raiz

    def mostrarraiz(self):
        if self.__raiz is not None:
            return self.__raiz.get_item()
        return None

    def insertar(self, elem, punt):
        if punt is None:
            return
        
        if elem < punt.get_item():
            if punt.get_izq() is None:
                nuevo = Nodo()
                nuevo.set_item(elem)
                punt.set_izq(nuevo)
            else:
                self.insertar(elem, punt.get_izq())
                
        elif elem > punt.get_item():
            if punt.get_der() is None:
                nuevo = Nodo()
                nuevo.set_item(elem)
                punt.set_der(nuevo)
            else:
                self.insertar(elem, punt.get_der())

        else:
            punt.incrementar_cont()

    #Imprimimos de menor a mayor
    def InOrden(self, punt):
        if punt is not None:
            self.InOrden(punt.get_izq())
            print(punt.get_item())
            self.InOrden(punt.get_der())

    def buscar(self, x):
        return self.buscar_aux(x, self.__raiz)

    def buscar_aux(self, x, punt):
        # La búsqueda compara el valor con la clave del nodo y avanza recursivamente
        if punt is None:
            return False
        if x == punt.get_item():
            return True
        elif x < punt.get_item():
            return self.buscar_aux(x, punt.get_izq())
        else:
            return self.buscar_aux(x, punt.get_der())

    #Calculamos la profundidad máxima del arbol
    def calcular_altura(self, punt):
        if punt is None:
            return 0
        else:
            m1 = self.calcular_altura(punt.get_izq())
            m2 = self.calcular_altura(punt.get_der())
            return max(m1, m2) + 1

    #Obtenemos la altura de un elemento x
    def get_altura(self, x):
        return self.nivel_altura(x, self.__raiz, 1)

    def nivel_altura(self, x, punt, actual):
        if punt is None:
            return -1
        if x == punt.get_item():
            return actual
        elif x < punt.get_item():
            return self.nivel_altura(x, punt.get_izq(), actual + 1)
        else:
            return self.nivel_altura(x, punt.get_der(), actual + 1)

    def get_cantidad_nodos(self, punt):
        if punt is None:
            return 0
        return 1 + self.get_cantidad_nodos(punt.get_izq()) + self.get_cantidad_nodos(punt.get_der())

    def borrar(self, x):
        self.__raiz = self.suprimir(self.__raiz, x)

    def suprimir(self, punt, x):
        if punt is None:
            return punt

        if x < punt.get_item():
            punt.set_izq(self.suprimir(punt.get_izq(), x))

        elif x > punt.get_item():
            punt.set_der(self.suprimir(punt.get_der(), x))

        else:
            if punt.get_cont() > 1:
                punt.decrementar_cont()
                return punt

            if punt.get_izq() is None:
                return punt.get_der()
            elif punt.get_der() is None:
                return punt.get_izq()

            #Si el grado es 2, se busca el máximo del subárbol izquierdo para el reemplazo
            aux = self.get_maximo(punt.get_izq())
            punt.set_item(aux.get_item())
            #Eliminamos el nodo maximo que acabamos de crear
            punt.set_izq(self.suprimir(punt.get_izq(), aux.get_item()))

        return punt

    def get_maximo(self, punt):
        actual = punt
        while actual.get_der() is not None:
            actual = actual.get_der()

        return actual


if __name__ == '__main__':
    arbol1 = arbol()
