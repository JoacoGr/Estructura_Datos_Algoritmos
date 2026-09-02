from Cola_Enlazada import cola
import random
from Trabajo import trabajo

def eje_5():
    impresora = cola()
    inicio = 0
    fin = 60
    actual = None
    limite = 0
    finalizados = 0
    espera = 0
    no_finalizados = 0

    while inicio < fin:

        if inicio % 5 == 0:
            proyecto = trabajo(random.randint(1,10))
            impresora.insertar(proyecto)

        if not impresora.vacio() and actual is None:
            actual = impresora.suprimir()
            limite = 0

        if actual is not None:
            actual.set_tiempo()
            limite += 1
            if actual.get_tiempo() <= 0:
                actual.set_fin()
                finalizados += 1
                espera += actual.get_espera()
                actual = None
                limite = 0
            elif limite == 5:
                impresora.insertar(actual)
                actual = None
                limite = 0

        if not impresora.vacio():
            aux = impresora.get_inicio()
            while aux is not None:
                aux.get_item().set_espera()
                aux = aux.get_sig()

        inicio += 1

    if actual is not None:
        no_finalizados += 1

    if not impresora.vacio():
        aux = impresora.get_inicio()
        while aux is not None:
            no_finalizados += 1
            aux = aux.get_sig()

    print(f"No finalizados: {no_finalizados}")

    if finalizados != 0:
        print(f'El tiempo promedio de ejecucion es de {espera / finalizados}')
    else: print("Ningun trabajo logró finalizar")

        

if __name__ == '__main__':
    eje_5()