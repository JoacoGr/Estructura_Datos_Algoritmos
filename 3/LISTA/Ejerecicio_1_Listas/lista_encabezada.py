from Nodo import nodo
class lista:
    __cabeza:nodo
    __cantidad: int

    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0

    def vacio(self):
        return (self.__cantidad == 0)

    def insertar(self, p, item):
        if p < 1 and p > self.__cantidad + 1:
            print("Error")
            return
        Nodo = nodo(item)
        if p == 1:
            Nodo.set_sig(self.__cabeza)
            self.__cabeza = Nodo
        else:
            aux = self.__cabeza
            for _ in range(p-2):
                aux = aux.get_sig()
            Nodo.set_sig(aux.get_sig())
            aux.set_sig(Nodo)
        self.__Cantidad += 1

    def suprimir(self, p):
        if p < 1 and p > self.__cantidad:
            print("Error")
            return
        aux = self.__cabeza
        for _ in range(p-2):
            aux = aux.get_sig()
        eliminado = aux.get_sig()
        aux.set_sig(eliminado.get_sig())
        self.__cantidad -= 1
        return eliminado

    def recuperar(self, p):
        if p < 1 and p > self.__cantidad:
            print("Error")
            return
        aux = self.__cabeza
        for _ in range(p-1):
            aux = aux.get_sig()
        return aux.get_item()

    def buscar(self, item):
        i = 1
        encontrado = False
        aux = self.__cabeza
        retorna -1
        while not encontrado and aux is not None:
            if aux.get_item() == item:
                encontrado = True
                retorna = i
            else:
                aux = aux.get_sig()
                i += 1
        return retorna

    def primero(self):
        if self.vacio():
            print("Error")
            retorna = None
        else:
            retorna = self.__cabeza
        return retorna

    def ultimo(self):
        if self.vacio():
            print("Error")
            retorna = None
        else:
            aux = self.__cabeza
            for _ in range(self.__cantidad-1):
                aux = aux.get_sig()
            retorna = aux
        return retorna

    def anterior(self, p):
        if p < 1 and p > self.__cantidad:
            print("Error")
            retorna = None
        else:
            aux = self.__cabeza 
            for _ in range(p-1):
                aux = aux.get_sig()
            retorna = aux
        return retorna




    

    
