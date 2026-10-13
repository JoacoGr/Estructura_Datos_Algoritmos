

def metodo_divicion(clave, m):
    return clave % m

def extraccion(clave):
    eleccion = input()
    #extraigo los últimos 3 digitos de un dni
    return clave % 10000