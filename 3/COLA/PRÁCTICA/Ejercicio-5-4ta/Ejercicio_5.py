from Cola_Enlazada import cola
from Proyecto import proyecto
import random
def ejercicio_5():
    impresora = cola()
    finalizados = 0
    inicio = 0
    fin = 60
    actual = None
    transcurrido = 0
    tiempo_permitido = 5
    espera = 0
    no_finalizados = 0

    while inicio < fin:
        if inicio % 5 == 0:
            usuario = proyecto(random.randint(1,10))
            impresora.insertar(usuario)

        if not impresora.vacio() and actual is None:
            actual = impresora.suprimir()
            transcurrido = 0

        if actual is not None:
            actual.set_tiempo()
            transcurrido += 1
            if actual.get_tiempo() <= 0:
                finalizados += 1
                actual.set_fin()
                espera += actual.get_espera()
                actual = None
                transcurrido = 0
            elif transcurrido == tiempo_permitido:
                impresora.insertar(actual)
                actual = None 
                transcurrido = 0

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

    print(f"La cantidad de proytectos no finalizados es de {no_finalizados}")
    print(f"El promedio de espera es de {espera / finalizados}")


if __name__ == '__main__':
    ejercicio_5()