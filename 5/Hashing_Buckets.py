import numpy as np

class HashBuckets:
    def __init__(self, M, b):
        """
        - __M: Cantidad de buckets en el Área Primaria.
        - __b: Capacidad máxima de registros por bucket.
        - __tam_overflow: Dimensión del Área de overflow (~20% del Área Primaria).
        - __total_buckets: Capacidad total de buckets (Primaria + overflow).
        - __registros: Matriz 2D de NumPy para almacenar las claves en filas y columnas.
        - __contadores: Arreglo 1D de NumPy para registrar la cantidad de claves por bucket.
        """
        self.__M = M
        self.__b = b
        self.__tam_overflow = int(np.ceil(M * 0.20)) # Garantiza al menos un bucket de desborde
        self.__total_buckets = self.__M + self.__tam_overflow
        
        # Matriz 2D para almacenar los registros de cada bucket
        self.__registros = np.zeros((self.__total_buckets, self.__b), dtype=int)
        
        # Arreglo 1D de contadores para cada bucket
        self.__contadores = np.zeros(self.__total_buckets, dtype=int)

    def hash_division(self, k):
        return k % self.__M

    def insertar(self, k):
        d = self.hash_division(k)
        insertado = False

        # 1. Comprobar si hay espacio disponible en el Área Primaria
        if self.__contadores[d] < self.__b:
            pos = self.__contadores[d]
            self.__registros[d, pos] = k
            self.__contadores[d] += 1
            insertado = True
            print(f"[INSERTAR] Clave {k} -> Guardada en Área Primaria: Bucket {d}, Posición {pos}")
        else:
            # 2. Si el bucket primario está lleno, buscar celda libre en el Área de overflow
            print(f"[OVERFLOW] Bucket {d} lleno al insertar {k}. Buscando en Área de Overflow...")
            overflow = self.__M
            while overflow < self.__total_buckets and not insertado:
                if self.__contadores[overflow] < self.__b:
                    pos = self.__contadores[overflow]
                    self.__registros[overflow, pos] = k
                    self.__contadores[overflow] += 1
                    insertado = True
                    print(f"[INSERTAR] Clave {k} -> Guardada en Área de Overflow: Bucket {overflow}, Posición {pos}")
                else:
                    overflow += 1

        if not insertado:
            print(f"[ERROR] No se pudo insertar la clave {k}: Área de Overflow saturada.")

        return insertado

    def buscar(self, k):
        d = self.hash_division(k)
        encontrado = False

        # 1. Búsqueda secuencial en el bucket del Área Primaria
        pos = 0
        while pos < self.__contadores[d] and not encontrado:
            if self.__registros[d, pos] == k:
                encontrado = True
                print(f"[BUSCAR] Clave {k} -> ¡Encontrada en Área Primaria! (Bucket {d}, Posición {pos})")
            else:
                pos += 1

        # 2. Si no se encontró y el bucket primario alcanzó su límite, examinar overflow
        if not encontrado and self.__contadores[d] == self.__b:
            print(f"[BUSCAR] Clave {k} no está en Bucket {d} (está lleno). Revisando Overflow...")
            overflow = self.__M
            while overflow < self.__total_buckets and not encontrado:
                indice = 0
                while indice < self.__contadores[overflow] and not encontrado:
                    if self.__registros[overflow, indice] == k:
                        encontrado = True
                        print(f"[BUSCAR] Clave {k} -> ¡Encontrada en Área de Overflow! (Bucket {overflow}, Posición {indice})")
                    else:
                        indice += 1
                overflow += 1

        if not encontrado:
            print(f"[BUSCAR] Clave {k} -> NO encontrada (Búsqueda infructuosa)")

        return encontrado


if __name__ == "__main__":
    tabla = HashBuckets(4, 2)
    print("--- INSERCIONES ---")
    tabla.insertar(23)
    tabla.insertar(22)
    tabla.insertar(24)
    tabla.insertar(11)
    tabla.insertar(50)
    tabla.insertar(32)
    tabla.insertar(4)

    print("\n--- BÚSQUEDAS ---")
    tabla.buscar(11)
    tabla.buscar(23)
    tabla.buscar(4)
    tabla.buscar(66)