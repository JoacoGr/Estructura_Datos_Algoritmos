from Nodo import nodo
class lista:
    __cantidad:int
    __cabeza: nodo

    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0

    def vacio(self):
        return (self.__cantidad == 0)

    def insertar(self, otro, p):
        if p < 1 or p > self.__cantidad + 1:
            print("Error")
            return False

        Nodo = nodo(otro)

        if p == 1:
            Nodo.set_sig(self.__cabeza)
            self.__cabeza = Nodo
        else:
            aux = self.__cabeza
            for _ in range(p-2):
                aux = aux.get_sig()
            Nodo.set_sig(aux.get_sig())
            aux.set_sig(Nodo)
        self.__cantidad += 1
        return True

    def suprimir(self, p):
        if p < 1 or p > self.__cantidad:
            print("Error")
            return False

        if p == 1:
            eliminado = self.__cabeza
            self.__cabeza = self.__cabeza.get_sig()
        else:
            aux = self.__cabeza
            for _ in range(p-2):
                aux = aux.get_sig()
            eliminado = aux.get_sig()
            aux.set_sig(eliminado.get_sig())
        self.__cantidad -= 1
        return eliminado

    def recuperar(self, p):
        if p < 1 or p > self.__cantidad:
            print("Error")
            return False
        aux = self.__cabeza
        for _ in range(p-1):
            aux = aux.get_sig()
        return aux.get_item()
    
    def buscar(self, otro):
        aux = self.__cabeza
        cont = 1
        while aux is not None:
            if aux.get_item() == otro:
                return cont
            cont += 1
            aux = aux.get_sig()
        return -1

    def primero(self):
        if self.vacio():
            return None
        return self.__cabeza

    def ultimo(self):
        if self.vacio():
            return None
        aux = self.__cabeza 
        for _ in range(self.__cantidad -1):
            aux = aux.get_sig()
        return aux

    def siguiente(self, p):
        if p < 1 or p >= self.__cantidad:
            retornar = -1
        else: retornar = p+1
        return retornar

    def anterior(self, p):
        if p <= 1 or p > self.__cantidad:
            retornar = -1
        else: retornar = p-1
        return retornar

    def recorrer(self):
        aux = self.__cabeza
        for _ in range(self.__cantidad):
            print(aux.get_item())
            aux = aux.get_sig()


        