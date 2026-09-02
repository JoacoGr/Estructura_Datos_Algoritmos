from Cola_Enlazada import cola
from Trabajo import trabajo
import random

def ejercicio_5():
    impresora = cola()
    maximo = 60
    inicio = 0
    trabajo_actual = None
    tiempo_procesado = 0
    finalizados = 0
    espera = 0
    no_atendidos = 0
    while inicio < maximo:
        if inicio % 5 == 0:
            proyecto = trabajo(random.randint(1,10))
            impresora.insertar(proyecto)

        if trabajo_actual is None and not impresora.vacio():
            trabajo_actual = impresora.suprimir()
            tiempo_procesado = 0

        if trabajo_actual is not None:
            trabajo_actual.set_tiempo(1)
            tiempo_procesado += 1
            if trabajo_actual.get_tiempo() <= 0:
                trabajo_actual.set_finalizado(True)
                finalizados += 1
                espera += trabajo_actual.get_espera()
                trabajo_actual = None
                tiempo_procesado = 0

            elif tiempo_procesado == 5:
                impresora.insertar(trabajo_actual)
                trabajo_actual = None
                tiempo_procesado = 0

        if not impresora.vacio():
            aux = impresora.get_inicio()
            while aux is not None:
                aux.get_item().set_espera(1)
                aux = aux.get_sig()

        inicio += 1

    if trabajo_actual is not None:
        no_atendidos += 1

    no_atendidos = 0

    aux = impresora.get_inicio()
    while aux is not None:
        no_atendidos += 1
        aux = aux.get_sig()

    print(f"a) Cantidad de trabajos sin atender: {no_atendidos}")
    if finalizados > 0:
        promedio = espera / finalizados
        print(f"b) Promedio de espera de los trabajos impresos: {promedio:.2f} minutos")
    else:
        print("b) No se completó ningún trabajo.")


if __name__ == '__main__':
    ejercicio_5()