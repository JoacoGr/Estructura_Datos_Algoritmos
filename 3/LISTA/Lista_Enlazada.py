from Nodo import nodo
class lista:
    __cabeza: nodo
    __cantidad: int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0

    def vacio(self):
        return (self.__cantidad == 0)

    def insertar(self, otro, p):
        if p < 1 or p > self.__cantidad + 1:
            print("Error")
            return None

        Nodo = nodo(otro)
        if p == 1:
            Nodo.set_sig(self.__cabeza)
            self.__cabeza = Nodo
        else:
            aux = self.__cabeza
            for _ in range(p -2):
                aux = aux.get_sig()
            Nodo.set_sig(aux.get_sig())
            aux.set_sig(Nodo)
        self.__cantidad += 1

    def suprimir(self, p):
        if p < 1 or p > self.__cantidad or self.vacio():
            print("Error")
            return None
        if p == 1:
            eliminado = self.__cabeza
            self.__cabeza = self.__cabeza.get_sig()
        else:
            aux = self.__cabeza.get_sig()
            for _ in range(p-2):
                aux = aux.get_sig()

            nodo_a_eliminar = aux.get_sig()
            eliminado = nodo_a_eliminar.get_item()
            aux.get_sig() = nodo_a_eliminar.get_sig()

        self.__cantidad -= 1
        return eliminado


