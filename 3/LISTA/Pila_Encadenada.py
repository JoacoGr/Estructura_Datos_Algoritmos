from Nodo import nodo
class pila:
    __cant:int
    __cabeza: nodo

    def __init__(self):
        self.__cant = 0
        self.__cabeza = None

    def agregar(self, otro):
        Nodo = nodo(otro)
        Nodo.set_item(otro)
        Nodo.set_sig(self.__cabeza)
        self.__cabeza = Nodo
        self.__cant += 1
        return Nodo.get_item()

    def suprimir(self):
        parar = True
        if self.vacia():
            print("No se puede extraer nada de esta lista ya que está vacia")
            parar = False
            aux = 0
        if parar:
            x = self.__cabeza.get_item()
            self.__cabeza = self.__cabeza.get_sig()
            self.__cant -= 1
            aux = x
        return aux

    def mostrar(self):
        aux = self.__cabeza
        while aux != None:
            print(self.__cabeza.get_item())
            aux = aux.get_sig()

    def vacia(self):
        if self.__cabeza == None:
            aux = True
        else: aux = False
        return aux

    def mostrar(self):
        """Recorre e imprime la pila desde el tope hasta la base sin crear listas auxiliares."""
        if self.vacia():
            print("Pila vacia")
            return

        actual = self.__cabeza
        print("Tope: ", end="")
        while actual is not None:
            print(actual.get_item(), end=" -> " if actual.get_sig() is not None else "")
            actual = actual.get_sig()

if __name__ == '__main__':
    pila1 = pila()
    if pila1.vacia():
        print("Se encuentra vacia")
    else: print("Tiene objetos")
    pila1.mostrar()
    print("---------------")
    pila1.agregar(1)
    pila1.agregar(2)
    pila1.agregar(3)
    pila1.mostrar()
    print("---------------")
    pila1.suprimir()
    pila1.mostrar()
    print("---------------")
    if pila1.vacia():
        print("Se encuentra vacia")
    else: print("Tiene objetos")
    pila1.suprimir()
    pila1.suprimir()
    if pila1.vacia():
        print("Se encuentra vacia")
    else: print("Tiene objetos")
    pila1.mostrar()

