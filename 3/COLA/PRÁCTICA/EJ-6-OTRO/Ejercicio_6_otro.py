from Cola_Enlazada_6 import cola
from Cliente_6 import cliente
import random

def eje_6():
    inicio = 0
    fin = 120
    espera = 0
    finalizados = 0
    no_finalizados = 0
    actual1 = None
    actual2 = None
    actual3 = None
    cola1 = cola()
    cola2 = cola()
    cola3 = cola()
    maximo = 0
    no_espera = 0

    while inicio < fin:
        if inicio % 2 == 0:

            c1 = cola1.get_cant()
            c2 = cola2.get_cant()
            c3 = cola3.get_cant()

            minimo = min(c1, c2, c3)
            opciones = []

            if c1 == minimo:
                opciones.append(1)
            if c2 == minimo:
                opciones.append(2)
            if c3 == minimo:
                opciones.append(3)

            c = random.choice(opciones)
            match c:
                case 1:
                    Cliente = cliente(5)
                    cola1.insertar(Cliente)
                case 2:
                    Cliente = cliente(3)
                    cola2.insertar(Cliente)
                case 3:
                    Cliente = cliente(4)
                    cola3.insertar(Cliente)

        if not cola1.vacio() and actual1 is None:
            actual1 = cola1.suprimir()

        if actual1 is not None:
            actual1.set_tiempo()
            if actual1.get_tiempo() <= 0:
                finalizados += 1
                if actual1.get_espera() > maximo:
                    maximo = actual1.get_espera()
                espera += actual1.get_espera()
                actual1 = None

        if not cola1.vacio():
            aux = cola1.get_inicio()
            while aux is not None:
                aux.get_item().set_espera()
                aux = aux.get_sig()


        if not cola2.vacio() and actual2 is None:
            actual2 = cola2.suprimir()

        if actual2 is not None:
            actual2.set_tiempo()
            if actual2.get_tiempo() <= 0:
                finalizados += 1
                if actual2.get_espera() > maximo:
                    maximo = actual2.get_espera()
                espera += actual2.get_espera()
                actual2 = None

        if not cola2.vacio():
            aux = cola2.get_inicio()
            while aux is not None:
                aux.get_item().set_espera()
                aux = aux.get_sig()


        if not cola3.vacio() and actual3 is None:
            actual3 = cola3.suprimir()

        if actual3 is not None:
            actual3.set_tiempo()
            if actual3.get_tiempo() <= 0:
                finalizados += 1
                if actual3.get_espera() > maximo:
                    maximo = actual3.get_espera()
                espera += actual3.get_espera()
                actual3 = None

        if not cola3.vacio():
            aux = cola3.get_inicio()
            while aux is not None:
                aux.get_item().set_espera()
                aux = aux.get_sig()


        inicio += 1

    print(f"El tiempo máximo de espera de un cliente fue de {maximo}")
    print(f"Los clientes atendidos fueron {finalizados}")

    if not cola1.vacio():
        aux = cola1.get_inicio()
        while aux is not None:
            no_finalizados += 1
            no_espera += aux.get_item().get_espera()
            aux = aux.get_sig()
    if not cola2.vacio():
        aux = cola2.get_inicio()
        while aux is not None:
            no_finalizados += 1
            no_espera += aux.get_item().get_espera()
            aux = aux.get_sig()
    if not cola3.vacio():
        aux = cola3.get_inicio()
        while aux is not None:
            no_finalizados += 1
            no_espera += aux.get_item().get_espera()
            aux = aux.get_sig()

    for actual in (actual1, actual2, actual3):
        if actual is not None:
            no_finalizados += 1
            no_espera += actual.get_espera()
            if actual.get_espera() > maximo:
                maximo = actual.get_espera()

    print(f"Los clientes que no llegaron a ser atendidos en el plazo de 2hs fueron {no_finalizados}")
    print(f"El promedio de espera de los clientes atendidos fue de {espera / finalizados}")
    if no_finalizados == 0:
        print("No quedó gente sin atender")
    else:
        print(f"El promedio de espera de los clientes no atendidos fue de {no_espera / no_finalizados}")


if __name__ == '__main__':
    eje_6()