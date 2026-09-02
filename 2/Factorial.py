from Pila_secuencial import pila

def factorial():
    n = int(input("Ingrese un número: "))
    pila1 = pila(n)
    for i in range(n, 0, -1):
        pila1.insertar(i)
    fac = 1
    while not pila1.vacio():
        valor = pila1.suprimir()
        fac *= valor
    print(f"El factorial es {fac}")
    
       
if __name__ == "__main__":
    factorial()