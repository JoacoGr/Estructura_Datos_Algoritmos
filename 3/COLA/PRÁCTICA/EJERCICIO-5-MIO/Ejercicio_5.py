from Cola_enlazada import cola
from Trabajo import trabajo
import random
def eje_5():
    impresora = cola()
    trabajo_actual = None
    inicio = 0
    fin = 60
    tiempo_procesado = 0
    espera = 0
    finalizados = 0
    while inicio < fin:

        if inicio % 5 == 0:
            proyecto = trabajo(random.randint(1,10))
            impresora.insertar(proyecto)

        if not impresora.vacio() and trabajo_actual == None:
            trabajo_actual = impresora.suprimir()
            tiempo_procesado = 0

        if trabajo_actual is not None:
            trabajo_actual.set_tiempo(1)
            tiempo_procesado += 1
            if trabajo_actual.get_tiempo() <= 0:
                trabajo_actual.set_finalizado()
                finalizados += 1
                espera += trabajo_actual.get_espera()
                trabajo_actual = None
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

    no_terminados = 0
    if trabajo_actual is not None:
        no_terminados += 1

    aux = impresora.get_inicio()
    while aux is not None:
        no_terminados +=1
        aux = aux.get_sig()

    print(f'Los trabajos no terminados son {no_terminados}')
    if finalizados > 0:
        print(f"El tiempo promedio de espera es de {espera / finalizados}")
    else: print('No se completó ningun trabajo')



        



if __name__ == '__main__':
    eje_5()