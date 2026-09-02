from Pila_secuencial import pila

def hanoi(pila1, pila2, pila3, n):
    jugando = True
    while jugando:
        envio = int(input("\nIngrese desde dónde mueve (1, 2, 3): "))
        recibo = int(input("Ingrese a qué columna se dirige (1, 2, 3): "))
        
        pilas = {1: pila1, 2: pila2, 3: pila3}
        
        if envio in pilas and recibo in pilas and envio != recibo:
            uno_a_otro(pilas[envio], pilas[recibo])
        else:
            print("Movimiento o columna incorrecta.")
        
        print("\n--- Estado de Pila 3 ---")
        pila3.mostrar()

        if comprobar(pila3, n):
            print("\n¡Felicidades! Has completado la torre de Hanoi.")
            jugando = False

def comprobar(pila3, n):
    if pila3.get_tope() + 1 != n:
        return False
    
    for i in range(pila3.get_tope()):
        if pila3.devolver_items(i) <= pila3.devolver_items(i + 1):
            return False
    return True

def uno_a_otro(envio, recibo):
    if envio.vacio():
        print("La columna de origen está vacía.")
        return

    if recibo.vacio() or envio.get_ultimo() < recibo.get_ultimo():
        disco = envio.suprimir()
        recibo.insertar(disco)
    else:
        print("Movimiento inválido: No puede colocar un disco más grande sobre uno más pequeño.")

if __name__ == '__main__':
    n = int(input("Ingrese cantidad de discos: "))
    pila1 = pila(n)
    pila2 = pila(n)
    pila3 = pila(n)

    for i in range(n, 0, -1):
        pila1.insertar(i)
        
    print("\nEstado inicial Pila 1:")
    pila1.mostrar()
    
    hanoi(pila1, pila2, pila3, n)