import numpy as np
from nodo import Nodo

class HashEncabezado:
    def __init__(self, M):
        self.__M = M
        self.__T = np.empty(M, dtype=object)
        self.__T.fill(None)

    def hash_division(self, k):
        return k % self.__M

    def insertar(self, k):
        d = self.hash_division(k)
        print(f"Para el elemento {k} su dirección es {d}")

        nuevo_nodo = Nodo(k)

        if self.__T[d] is None:
            print(f"La posición {d} está vacía. Se inserta como primer elemento")
            self.__T[d] = nuevo_nodo
        else:
            print(f"Ya hay elementos en esa posición, encadenamos {k}")
            nuevo_nodo.set_sig(self.__T[d])
            self.__T[d] = nuevo_nodo

        print(f"Clave {k} insertada en la posición {d}")
        print("--------------------")

    def buscar(self, k):
        d = self.hash_division(k)
        print(f"Para el elemento {k} la direccion es {d}")

        actual = self.__T[d]

        # Si la cabeza es None, no hay ningún elemento en esa posición
        if actual is None:
            print(f"{k} no está en la tabla")
            return False

        pos_nodo = 1
        encontrado = False

        while actual is not None and not encontrado:
            print(f"  [Comparación {pos_nodo}] Clave actual en nodo: {actual.get_clave()}")
            if actual.get_clave() == k:
                print(f"Clave {k} encontrada")
                encontrado = True
            else:
                #No coincide. Avanzando al siguiente nodo
                actual = actual.get_sig()
                pos_nodo += 1

        if not encontrado:
            print(f"No se halló el elemento {k}")

        print("--------------------")
        return encontrado

if __name__ == "__main__":
    tabla = HashEncabezado(4)
    tabla.insertar(23)
    tabla.insertar(11)
    tabla.insertar(50)
    tabla.insertar(32)
    tabla.insertar(4)
    tabla.buscar(11)
    tabla.buscar(23)
    tabla.buscar(66)

