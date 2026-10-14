import numpy as np

class HashAbierto:
    def __init__(self, M):
        self.__M = M
        self.__claves = np.zeros(M, dtype=int)
        self.__ocupado = np.zeros(M, dtype=bool)
        self.__cantidad = 0

    def hash_division(self, k):
        return k % self.__M

    def insertar(self, k):
        # Si la tabla está saturada, no se puede insertar
        if self.__cantidad == self.__M:
            print(f"Tabla llena no se pudo insertar {k}")
            return False

        d = self.hash_division(k)
        pasos = 0
        insertado = False

        # Itera como máximo M veces sin usar break
        while pasos < self.__M and not insertado:
            if not self.__ocupado[d]:
                self.__claves[d] = k
                self.__ocupado[d] = True
                self.__cantidad += 1
                insertado = True
                print(f"Se insertó {k} en la posicion {d}")
            elif self.__claves[d] == k:
                # Si la clave ya existe, termina sin insertar
                return False
            else:
                d = (d + 1) % self.__M
                pasos += 1

        return insertado

    def buscar(self, k):
        d = self.hash_division(k)
        pasos = 0
        encontrado = False
        vacio_encontrado = False

        # Se detiene si lo encuentra, si halla celda vacía o si ya revisó las M posiciones
        while pasos < self.__M and not encontrado and not vacio_encontrado:
            if not self.__ocupado[d]:
                vacio_encontrado = True
            elif self.__claves[d] == k:
                encontrado = True
                print(f"Se halló {k} en la posicion {d}")
            else:
                d = (d + 1) % self.__M
                pasos += 1

        if not encontrado:
            print(f"No se halló el elemento {k} en la tabla hash")

        return encontrado


if __name__ == "__main__":
    tabla = HashAbierto(4)
    tabla.insertar(23)
    tabla.insertar(11)
    tabla.insertar(50)
    tabla.insertar(32)
    tabla.insertar(4)
    tabla.buscar(11)
    tabla.buscar(23)
    tabla.buscar(66)