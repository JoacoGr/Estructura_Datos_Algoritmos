from classNodo import nodo

class arbolB:
    __raiz: nodo

    def __init__(self):
        self.__raiz = None

    def getRaiz(self):
        return self.__raiz

    def setRaiz(self, raiz):
        self.__raiz = raiz

    def insertar(self, sub, clave):
        if sub is None:
            return nodo(clave)
        elif clave == sub.getClave():
            sub.incrementarCont(1)
        elif clave < sub.getClave():
            sub.setIzq(self.insertar(sub.getIzq(), clave))
        else:
            sub.setDer(self.insertar(sub.getDer(), clave))
        return sub

    def mayorNodo(self, sub):
        # Busca el nodo con la clave máxima (el más a la derecha del subárbol)
        actual = sub
        while actual.getDer() is not None:
            actual = actual.getDer()
        return actual

    def suprimir(self, sub, clave):
        if sub is None:
            return None
        elif clave < sub.getClave():
            sub.setIzq(self.suprimir(sub.getIzq(), clave))
        elif clave > sub.getClave():
            sub.setDer(self.suprimir(sub.getDer(), clave))
        else:
            # Caso 1 y 2: Sin hijo izquierdo o sin hijo derecho (cubre también hojas)
            if sub.getIzq() is None:
                return sub.getDer()
            elif sub.getDer() is None:
                return sub.getIzq()
            else:
                # Caso 3: Dos hijos -> Reemplazo por el mayor del subárbol izquierdo
                mayor = self.mayorNodo(sub.getIzq())
                sub.setClave(mayor.getClave())
                sub.setCont(mayor.getCont())
                sub.setIzq(self.suprimir(sub.getIzq(), mayor.getClave()))
        return sub

    def buscar(self, sub, x):
        if sub is None:
            return None
        elif x == sub.getClave():
            return sub
        elif x < sub.getClave():
            return self.buscar(sub.getIzq(), x)
        else:
            return self.buscar(sub.getDer(), x)

    def hijo(self, sub, KeySon):
        # Muestra el padre de KeySon si existe
        if sub is None:
            return None
        if (sub.getIzq() is not None and sub.getIzq().getClave() == KeySon) or \
           (sub.getDer() is not None and sub.getDer().getClave() == KeySon):
            print(f"El elemento {KeySon} es hijo de {sub.getClave()}")
            return sub
        elif KeySon < sub.getClave():
            return self.hijo(sub.getIzq(), KeySon)
        else:
            return self.hijo(sub.getDer(), KeySon)

    def cantNodos(self, sub):
        if sub is None:
            return 0
        return 1 + self.cantNodos(sub.getIzq()) + self.cantNodos(sub.getDer())

    def altura(self, sub):
        if sub is None:
            return -1
        return 1 + max(self.altura(sub.getIzq()), self.altura(sub.getDer()))

    def PreOrder(self, sub):
        if sub is not None:
            print(sub.getClave())
            self.PreOrder(sub.getIzq())
            self.PreOrder(sub.getDer())

    def InOrder(self, sub):
        if sub is not None:
            self.InOrder(sub.getIzq())
            print(sub.getClave())
            self.InOrder(sub.getDer())

    def PostOrder(self, sub):
        if sub is not None:
            self.PostOrder(sub.getIzq())
            self.PostOrder(sub.getDer())
            print(sub.getClave())


if __name__ == '__main__':
    arbol = arbolB()

    # Carga de claves
    for i in range(5):
        n = int(input("Clave: "))
        arbol.setRaiz(arbol.insertar(arbol.getRaiz(),  n))

    print("\nPreOrder inicial:")
    arbol.PreOrder(arbol.getRaiz())

    # Supresión
    n = int(input("\nClave a suprimir: "))
    arbol.setRaiz(arbol.suprimir(arbol.getRaiz(), n))

    print("\nPreOrder final:")
    arbol.PreOrder(arbol.getRaiz())

    print('----------------------------')
    print(f"{arbol.buscar(arbol.getRaiz(), 6)}")
    print(arbol.buscar(arbol.getRaiz(), 66))