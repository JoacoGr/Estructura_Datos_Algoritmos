import numpy as np
from Cola_Enlazada_2 import Cola
from Nodo_2 import nodo


class Grafo:
    __num_vertices: int
    __cabezas: np.ndarray
    __tiempo: int
    __tiene_ciclo: bool

    def __init__(self, num_vertices):
        self.__num_vertices = num_vertices
        self.__cabezas = np.empty(num_vertices + 1, dtype=object)
        self.__cabezas.fill(None)
        self.__tiempo = 0
        self.__tiene_ciclo = False

    def agregar_arista(self, u, v):
        nuevo_v = nodo(v)
        nuevo_v.set_sig(self.__cabezas[u])
        self.__cabezas[u] = nuevo_v

        nuevo_u = nodo(u)
        nuevo_u.set_sig(self.__cabezas[v])
        self.__cabezas[v] = nuevo_u

    def adyacentes(self, u):
        ady = []
        actual = self.__cabezas[u]
        while actual is not None:
            ady.append(actual.get_vertice())
            actual = actual.get_sig()
        return ady

    def bea(self, s):
        inf = float('inf')
        d = [inf] * (self.__num_vertices + 1)
        cola = Cola()

        d[s] = 0
        cola.insertar(s)

        while not cola.vacio():
            v = cola.suprimir()
            print(f"Procesando vértice: {v} (distancia: {d[v]})")
            for u in self.adyacentes(v):
                if d[u] == inf:
                    d[u] = d[v] + 1
                    cola.insertar(u)

    def __bep_visita(self, s, d, f):
        self.__tiempo += 1
        d[s] = self.__tiempo
        print(f"Descubierto vértice: {s} (tiempo: {d[s]})")

        for u in self.adyacentes(s):
            if d[u] == 0:
                self.__bep_visita(u, d, f)

        self.__tiempo += 1
        f[s] = self.__tiempo
        print(f"Finalizado vértice: {s} (tiempo: {f[s]})")

    def bep(self):
        d = [0] * (self.__num_vertices + 1)
        f = [0] * (self.__num_vertices + 1)
        self.__tiempo = 0

        for s in range(1, self.__num_vertices + 1):
            if d[s] == 0:
                self.__bep_visita(s, d, f)

    def camino(self, u, v):
        inf = float('inf')
        d = [inf] * (self.__num_vertices + 1)
        padre = [None] * (self.__num_vertices + 1)
        cola = Cola()

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
        if self.__num_vertices == 0:
            return True

        inf = float('inf')
        d = [inf] * (self.__num_vertices + 1)
        cola = Cola()

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

    def __aciclico_visita(self, s, d, padre):
        self.__tiempo += 1
        d[s] = self.__tiempo

        for u in self.adyacentes(s):
            if d[u] == 0:
                padre[u] = s
                self.__aciclico_visita(u, d, padre)
            elif u != padre[s]:
                self.__tiene_ciclo = True

    def aciclico(self):
        d = [0] * (self.__num_vertices + 1)
        padre = [None] * (self.__num_vertices + 1)
        self.__tiempo = 0
        self.__tiene_ciclo = False

        for s in range(1, self.__num_vertices + 1):
            if d[s] == 0 and not self.__tiene_ciclo:
                self.__aciclico_visita(s, d, padre)

        return not self.__tiene_ciclo


if __name__ == "__main__":
    grafo = Grafo(4)
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