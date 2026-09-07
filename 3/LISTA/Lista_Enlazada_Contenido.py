from Nodo import nodo
class lista:
    __cabeza: nodo
    __cantidad: int

    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0

    def vacio(self):
        return (self.__cantidad == 0)

    def insertar(self, otro):
            Nodo = nodo(otro)

            if self.__cabeza is None or otro < self.__cabeza.get_item():
                Nodo.set_sig(self.__cabeza)
                self.__cabeza = Nodo
                self.__cantidad += 1
                return

            aux = self.__cabeza
            while aux.get_sig() is not None and aux.get_sig().get_item() < otro:
                aux = aux.get_sig()

            Nodo.set_sig(aux.get_sig())
            aux.set_sig(Nodo)
            self.__cantidad += 1
            return 

    def suprimir(self, otro):
        aux = self.__cabeza
        terminado = True
        while aux is not None and terminado:
            if aux.get_sig().get_item() == otro:
                eliminado = aux.get_sig()
                aux.set_sig(eliminado.get_sig())
                terminado = False
            aux = aux.get_sig()
        if terminado:
            print("No se halló el objeto a eliminar")
            return


    def recuperar(self, otro):
        aux = self.__cabeza
        cont = 0
        while aux is not None and aux.get_item() is not otro:
            cont +=1
            aux = aux.get_sig()
        return cont


    def mostrar(self):
        aux = self.__cabeza
        while aux is not None:
            print(aux.get_item())
            aux = aux.get_sig()


if __name__ == '__main__':
    lista1 = lista()
    lista1.insertar(1)
    lista1.insertar(8)
    lista1.insertar(3)
    lista1.insertar(6)
    lista1.insertar(5)
    lista1.suprimir(3)
    print("---------------")
    print(lista1.recuperar(8))