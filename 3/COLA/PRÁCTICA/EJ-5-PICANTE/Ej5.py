from Cola_Enlazada_Picante import cola
from Proyecto import proyecto
import random

def eje5():
    inicio = 0
    fin = 60
    espera = 0
    actual = None
    no_finalizados = 0
    finalizados = 0
    transcurrido = 0
    impresora = cola()

    while inicio < fin:
        if inicio % 5 == 0:
            Proyecto = proyecto(random.randint(1,10))
            impresora.insertar(Proyecto)

        if not impresora.vacio() and actual is None:
            actual = impresora.suprimir()
            transcurrido = 0

        if not impresora.vacio():
            aux = impresora.get_inicio()
            while aux is not None:
                aux.get_item().set_espera()
                aux = aux.get_sig()

        if actual is not None:
            actual.set_tiempo()
            transcurrido += 1
            if actual.get_tiempo() <= 0:
                finalizados += 1
                espera += actual.get_espera()
                transcurrido = 0
                actual = None
            elif transcurrido == 5:
                impresora.insertar(actual)
                transcurrido = 0
                actual = None

        inicio += 1

    if not impresora.vacio():
        aux = impresora.get_inicio()
        while aux is not None:
            no_finalizados += 1
            aux = aux.get_sig()

    if actual is not None:
        no_finalizados += 1

    print(f"Los trabajos que no lograron finalizar son {no_finalizados}")
    if finalizados > 0:
        print(f"El promedio de espera de los trabajos finalizados es de {espera / finalizados:.2f}")
    else:
        print("No se terminó ningún trabajo durante la simulación.")



if __name__ == '__main__':
    eje5()