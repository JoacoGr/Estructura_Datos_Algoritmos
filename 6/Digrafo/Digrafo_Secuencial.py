import numpy as np
from Cola_Secuencial_Cir_2 import Cola

class Digrafo:
    __num_vertices: int
    __A: np.ndarray
    __tiempo: int
    __tiene_ciclo: bool
    __lista_topologica: list

    def __init__(self, num_vertices):
        self.__num_vertices = num_vertices
        # Matriz de (|V| + 1) x (|V| + 1) inicializada en 0 con NumPy
        self.__A = np.zeros((num_vertices + 1, num_vertices + 1), dtype=int)
        self.__tiempo = 0
        self.__tiene_ciclo = False
        self.__lista_topologica = []

    def agregar_arista(self, u, v):
        # En un digrafo el arco tiene dirección de u hacia v
        self.__A[u, v] = 1

    def grado_salida(self, u):
        """Número de aristas que empiezan en u."""
        return np.sum(self.__A[u, :])

    def grado_entrada(self, u):
        """Número de aristas que terminan en u."""
        return np.sum(self.__A[:, u])

    def adyacentes(self, u):
        ady = []
        for v in range(1, self.__num_vertices + 1):
            if self.__A[u, v] == 1:
                ady.append(v)
        return ady

    def bea(self, s):
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

    def __bep_visita(self, s, d, f):
        self.__tiempo += 1
        d[s] = self.__tiempo
        print(f"Descubierto vértice: {s} (tiempo: {d[s]})")

        for u in self.adyacentes(s):
            if d[u] == 0:
                self.__bep_visita(u, d, f)

        self.__tiempo += 1
        f[s] = self.__tiempo
        # Ordenación Topológica: insertar a la cabeza de la lista conforme son terminados
        self.__lista_topologica.insert(0, s)
        print(f"Finalizado vértice: {s} (tiempo: {f[s]})")

    def bep(self):
        d = [0] * (self.__num_vertices + 1)
        f = [0] * (self.__num_vertices + 1)
        self.__tiempo = 0
        self.__lista_topologica = []

        for s in range(1, self.__num_vertices + 1):
            if d[s] == 0:
                self.__bep_visita(s, d, f)

    def ordenacion_topologica(self):
        """Devuelve la ordenación topológica ejecutando BEP."""
        self.bep()
        return self.__lista_topologica

    def camino(self, u, v):
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

    def fuertemente_conexo(self):
        """Evalúa si es fuertemente conexo asegurando que todo par es mutuamente alcanzable."""
        if self.__num_vertices == 0:
            return True

        for s in range(1, self.__num_vertices + 1):
            inf = float('inf')
            d = [inf] * (self.__num_vertices + 1)
            cola = Cola(self.__num_vertices + 1)
            
            d[s] = 0
            cola.insertar(s)

            while not cola.vacio():
                v = cola.suprimir()
                for u in self.adyacentes(v):
                    if d[u] == inf:
                        d[u] = d[v] + 1
                        cola.insertar(u)

            # Si desde el nodo 's' actual no se alcanzó algún nodo, no es fuertemente conexo
            for i in range(1, self.__num_vertices + 1):
                if d[i] == inf:
                    return False
        return True

    def __aciclico_visita(self, s, d, padre, en_proceso):
        self.__tiempo += 1
        d[s] = self.__tiempo
        en_proceso[s] = True

        for u in self.adyacentes(s):
            if d[u] == 0:
                padre[u] = s
                self.__aciclico_visita(u, d, padre, en_proceso)
            elif en_proceso[u]:
                # Arista hacia un nodo descubierto pero no terminado (arista hacia atrás)
                self.__tiene_ciclo = True

        en_proceso[s] = False

    def aciclico(self):
        d = [0] * (self.__num_vertices + 1)
        padre = [None] * (self.__num_vertices + 1)
        en_proceso = [False] * (self.__num_vertices + 1)
        self.__tiempo = 0
        self.__tiene_ciclo = False

        for s in range(1, self.__num_vertices + 1):
            if d[s] == 0 and not self.__tiene_ciclo:
                self.__aciclico_visita(s, d, padre, en_proceso)

        return not self.__tiene_ciclo


if __name__ == "__main__":
    # Prueba armando un dígrafo simple (por ejemplo: 1->2, 1->3, 3->4)
    digrafo = Digrafo(4)
    digrafo.agregar_arista(1, 2)
    digrafo.agregar_arista(1, 3)
    digrafo.agregar_arista(3, 4)

    print("Adyacentes a 1:", digrafo.adyacentes(1))
    print("Grado de salida nodo 1:", digrafo.grado_salida(1))
    print("Grado de entrada nodo 2:", digrafo.grado_entrada(2))
    print("¿Es fuertemente conexo?:", digrafo.fuertemente_conexo())
    print("¿Es acíclico?:", digrafo.aciclico())
    if digrafo.aciclico():
        print("Ordenación topológica:", digrafo.ordenacion_topologica())
    print("----------------------")
    print("Camino de 1 a 4:", digrafo.camino(1, 4))