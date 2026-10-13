import numpy as np
from nodo import Nodo
class hash:
    __dim: int
    __tabla: np.ndarray

    def __init__(self, dim):
        self.__dim = dim
        self.__tabla = np.empty(dim, dtype=object)

    def insertar(self, clave):
        posicion = self.metodo_divicion(clave)
