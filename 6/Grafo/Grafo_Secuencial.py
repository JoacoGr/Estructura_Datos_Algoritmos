import numpy as np
from Cola_Secuencial_Cir_2 import Cola

class GrafoMatriz:
    __num_vertices: int
    __A: np.ndarray

    def __init__(self, num_vertices):
        self.__num_vertices = num_vertices
        # Matriz de (|V| + 1) x (|V| + 1) inicializada completamente en 0
        self.__A = np.zeros((num_vertices + 1, num_vertices + 1), dtype=int)

    def agregar_arista(self, u, v):
        self.__A[u, v] = 1
        self.__A[v, u] = 1

    def adyacentes(self, u):
        """Determina los nodos adyacentes de u."""
        ady = []
        for v in range(1, self.__num_vertices + 1):
            if self.__A[u, v] == 1:
                ady.append(v)
        return ady

    def bea(self, s):
        """Procesa todos los elementos en anchura."""
        inf = float('inf')
        d = [inf] * (self.__num_vertices + 1)
        cola = Cola(self.__num_vertices + 1)

        d[s] = 0
        cola.insertar(s)

        while not cola.vacio():
            v = cola.suprimir()
            print(f"Procesando vértice: {v} (distancia: {d[v]})")
            for u in self.adyacentes(v):
                if d[u] == inf:
                    d[u] = d[v] + 1
                    cola.insertar(u)

    def bep(self):
        """Procesa todos los elementos en profundidad."""
        d = [0] * (self.__num_vertices + 1)
        f = [0] * (self.__num_vertices + 1)
        tiempo = 0

        def bep_visita(s):
            nonlocal tiempo
            tiempo += 1
            d[s] = tiempo
            print(f"Descubierto vértice: {s} (tiempo: {d[s]})")

            for u in self.adyacentes(s):
                if d[u] == 0:
                    bep_visita(u)

            tiempo += 1
            f[s] = tiempo
            print(f"Finalizado vértice: {s} (tiempo: {f[s]})")

        for s in range(1, self.__num_vertices + 1):
            if d[s] == 0:
                bep_visita(s)

    def camino(self, u, v):
        """Determina el camino de u a v usando el árbol de BEA."""
        inf = float('inf')
        d = [inf] * (self.__num_vertices + 1)
        padre = [None] * (self.__num_vertices + 1)
        cola = Cola(self.__num_vertices + 1)

        d[u] = 0
        cola.insertar(u)

        while not cola.vacio():
            x = cola.suprimir()
            for w in self.adyacentes(x):
                if d[w] == inf:
                    d[w] = d[x] + 1
                    padre[w] = x
                    cola.insertar(w)

        if d[v] == inf:
            raise ValueError(f"Error: {v} no es alcanzable desde {u}")

        camino_res = []
        actual = v
        while actual is not None:
            camino_res.append(actual)
            actual = padre[actual]
        camino_res.reverse()
        return camino_res

    def conexo(self):
        """Evalúa si G es conexo."""
        if self.__num_vertices == 0:
            return True

        inf = float('inf')
        d = [inf] * (self.__num_vertices + 1)
        cola = Cola(self.__num_vertices + 1)

        d[1] = 0
        cola.insertar(1)

        while not cola.vacio():
            v = cola.suprimir()
            for u in self.adyacentes(v):
                if d[u] == inf:
                    d[u] = d[v] + 1
                    cola.insertar(u)

        for i in range(1, self.__num_vertices + 1):
            if d[i] == inf:
                return False
        return True

    def aciclico(self):
        """Evalúa si G es acíclico detectando aristas hacia atrás con BEP."""
        d = [0] * (self.__num_vertices + 1)
        padre = [None] * (self.__num_vertices + 1)
        tiempo = 0
        tiene_ciclo = False

        def aciclico_visita(s):
            nonlocal tiempo, tiene_ciclo
            tiempo += 1
            d[s] = tiempo

            for u in self.adyacentes(s):
                if d[u] == 0:
                    padre[u] = s
                    aciclico_visita(u)
                elif u != padre[s]:
                    tiene_ciclo = True

        for s in range(1, self.__num_vertices + 1):
            if d[s] == 0 and not tiene_ciclo:
                aciclico_visita(s)

        return not tiene_ciclo


if __name__ == "__main__":
    grafo = GrafoMatriz(4)
    grafo.agregar_arista(1, 2)
    grafo.agregar_arista(1, 3)
    grafo.agregar_arista(3, 2)
    grafo.agregar_arista(3, 4)

    print("Adyacentes a 1:", grafo.adyacentes(1))
    print("¿Es conexo?:", grafo.conexo())
    print("Camino de 1 a 4:", grafo.camino(1, 4))
    print("¿Es acíclico?:", grafo.aciclico())
    print("----------------------")
    grafo.bea(1)