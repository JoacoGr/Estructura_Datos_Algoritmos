from Cola_Enlazada import cola
import random
class proyecto:
    __espera: int
    __tiempo: int
    __numero: int
    __atendido: bool

    def __init__(self, total, inicio, i):
        self.__espera = inicio
        self.__tiempo = total
        self.__numero = i
        self.__atendido = False

    def get_numero(self):
        return int(self.__numero)

    def get_espera(self):
        return int(self.__espera)

    def get_tiempo(self):
        return int(self.__tiempo)

    def get_atendido(self):
        return self.__atendido

    def incrementar_espera(self):
        if not self.__atendido:
            self.__espera += 1

    def set_espera(self, espe):
        self.__espera += espe

    def set_tiempo(self, tiempo):
        self.__tiempo = tiempo

def eje_impresora():
    impresora = cola()
    frecuencia = 60
    inicio = 0
    while True:

        



if __name__ == '__main__':
    eje_impresora()