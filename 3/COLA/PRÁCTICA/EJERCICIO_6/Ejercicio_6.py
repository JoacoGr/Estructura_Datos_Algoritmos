from Cola_Enlazada import cola
from Clientes import cliente
import random

def eje_6():
    cajero1 = cola()
    cajero2 = cola()
    cajero3 = cola()
    inicio = 0
    fin = 120
    finalizados = 0
    no_atendidos = 0
    si_espera = 0
    no_espera = 0
    maximo = 0
    actual1 = None
    actual2 = None
    actual3 = None

    while inicio < fin:
        if inicio % 2 == 0:
            c1 = cajero1.get_cant()
            c2 = cajero2.get_cant()
            c3 = cajero3.get_cant()
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
                    usuario1 = cliente(5)
                    cajero1.insertar(usuario1)
                case 2:
                    usuario2 = cliente(3)
                    cajero2.insertar(usuario2)
                case 3:
                    usuario3 = cliente(4)
                    cajero3.insertar(usuario3)

            if not cajero1.vacio() and actual1 is None:
                actual1 = cajero1.suprimir()
                transcurrido1 = 0

            if actual1 is not None:
                transcurrido1 +=1
                actual1.set_tiempo()
                if actual1.get_tiempo() <= 0:
                    actual1.set_fin()
                    finalizados += 1
                    si_espera += actual1.get_espera()
                    if actual1.get_espera() > maximo:
                        maximo = actual1.get_espera()
                    actual1 = None
                    transcurrido1 = 0

            if not cajero1.vacio():
                aux = cajero1.get_inicio()
                while aux is not None:
                    aux.get_item().set_espera()
                    aux = aux.get_sig()
                
            trancurrido2 = 0
            if inicio % 3 == 0:
                usuario2 = cliente(3)
                cajero2.insertar(usuario2)

            if not cajero2.vacio() and actual2 is None:
                actual2 = cajero2.suprimir()
                transcurrido2 = 0

            if actual2 is not None:
                actual2.set_tiempo()
                transcurrido2 += 1
                if actual2.get_tiempo() <= 0:
                    finalizados += 1
                    actual2.set_fin()
                    si_espera += actual2.get_espera()
                    if actual2.get_espera() > maximo:
                        maximo = actual2.get_espera()
                    actual2 = None
                    transcurrido2 = 0

            if not cajero2.vacio():
                aux = cajero2.get_inicio()
                while aux is not None:
                    aux.get_item().set_espera()
                    aux = aux.get_sig()

            transcurrido3 = 0
            if inicio % 4 == 0:
                usuario3 = cliente(4)
                cajero3.insertar(usuario3)

            if not cajero3.vacio() and actual3 is None:
                actual3 = cajero3.suprimir()
                trancurrido3 = 0

            if actual3 is not None:
                actual3.set_tiempo()
                transcurrido3 += 1
                if actual3.get_tiempo() <= 0:
                    finalizados += 1
                    actual3.set_fin()
                    si_espera += actual3.get_espera()
                    if actual3.get_espera() > maximo:
                        maximo = actual3.get_espera()
                    actual3 = None
                    transcurrido3 = 0

            if not cajero3.vacio():
                aux = cajero3.get_inicio()
                while aux is not None:
                    aux.get_item().set_espera()
                    aux = aux.get_sig()

        inicio += 1

    if not cajero1.vacio():
        aux = cajero1.get_inicio()
        while aux is not None:
            no_atendidos += 1
            espera_cliente = aux.get_item().get_espera()
            no_espera += espera_cliente
            if espera_cliente > maximo:
                maximo = espera_cliente      
            aux = aux.get_sig()


    if not cajero2.vacio():
        aux = cajero2.get_inicio()
        while aux is not None:
            no_atendidos += 1
            no_espera += aux.get_item().get_espera()
            if aux.get_item().get_espera() > maximo:
                maximo = actual2.get_espera()
            aux = aux.get_sig()

    if not cajero3.vacio():
        aux = cajero3.get_inicio()
        while aux is not None:
            no_atendidos += 1
            no_espera += aux.get_item().get_espera()
            if aux.get_item().get_espera() > maximo:
                maximo = actual3.get_espera()
            aux = aux.get_sig()


    print(f"El tiempo máximo de espera fue de: {maximo}")
    print(f"La cantidad de clientes atendidos fue de {finalizados}")
    print(f"La cantidad de clientes no atendidos fue de {no_atendidos}")
    print(f"El promedio de espera entre los clientes atendidos fue de {si_espera/finalizados}")
    print(f"El promedio de espera entre los clientes no atendidos fue de {no_espera/no_atendidos}")

                        


                







            


if __name__ == '__main__':
    try:
        eje_6()
    except IndexError as e:
        print(e)