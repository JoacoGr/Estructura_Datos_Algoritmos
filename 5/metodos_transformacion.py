import numpy as np

def division(k, M):
    return k % M


def medio_del_cuadrado(k, M):
    """
    2. Método del Medio del Cuadrado (HASHING.pdf pág. 3; Diapo 12)
    Eleva la clave al cuadrado y extrae los dígitos centrales.
    Si no se especifica 'cant_digitos', se deduce a partir del orden de M.
    """
    cant_digitos = None
    cuadrado = k ** 2
    s = str(cuadrado)
    
    # Si no se especifica cuántos dígitos extraer, usamos los necesarios para indexar hasta M-1
    if cant_digitos is None:
        cant_digitos = len(str(M - 1))
        
    longitud = len(s)
    
    if longitud <= cant_digitos:
        direccion = int(s)
    else:
        # Calcular la posición central para recortar
        inicio = (longitud - cant_digitos) // 2
        fin = inicio + cant_digitos
        direccion = int(s[inicio:fin])
        
    # Asegurar que quede dentro del rango [0, M - 1]
    return direccion % M


def plegamiento_desplazado(k, M):
    """
    3.a. Plegamiento Desplazado / Fold Shifting (HASHING.pdf pág. 3; Diapo 13-14)
    Divide la clave en partes de tamaño fijo, las suma directamente
    y ajusta el resultado al espacio de la tabla.
    """
    tam_parte = None
    s = str(k)
    if tam_parte is None:
        tam_parte = len(str(M - 1))

    suma = 0
    i = 0
    while i < len(s):
        fragmento = s[i:i + tam_parte]
        suma += int(fragmento)
        i += tam_parte

    return suma % M


def plegamiento_limite(k, M):
    """
    3.b. Plegamiento Límite / Boundary Folding (HASHING.pdf pág. 3; Diapo 15)
    Divide la clave en partes; las partes extremas (o alternas) se invierten
    antes de sumarse, como si los límites se doblaran hacia el centro.
    """
    tam_parte = None
    s = str(k)
    if tam_parte is None:
        tam_parte = len(str(M - 1))

    partes = []
    i = 0
    while i < len(s):
        partes.append(s[i:i + tam_parte])
        i += tam_parte

    suma = 0
    for idx in range(len(partes)):
        # En pliegue límite, las partes impares o de los bordes se invierten
        if idx % 2 == 1:
            suma += int(partes[idx][::-1])
        else:
            suma += int(partes[idx])

    return suma % M

def extraccion(k, M):
    """
    4. Método de Extracción (HASHING.pdf pág. 4; Diapo 16)
    Selecciona posiciones específicas de los dígitos de la clave
    y los une para formar la dirección.
    'posiciones' recibe una lista de índices (base 0) a extraer.
    """
    posiciones: list = None
    s = str(k)
    
    # Si no se definen posiciones, por defecto extrae los últimos dígitos necesarios para M
    if posiciones is None:
        cant_digitos = len(str(M - 1))
        cadena_extraida = s[-cant_digitos:]
    else:
        digitos = []
        for p in posiciones:
            if p < len(s):
                digitos.append(s[p])
        cadena_extraida = "".join(digitos)
        if not cadena_extraida:
            cadena_extraida = "0"

    return int(cadena_extraida) % M

def palabra_a_entero(palabra):
    k = 0
    for caracter in palabra:
        k = k * 31 + ord(caracter)
    return k

if __name__ == "__main__":
    clave = 'Joaquin'
    M = 100

    if type(clave) is str:
        clave = palabra_a_entero(clave)

    print("=" * 60)
    print(f"PRUEBA DE MÉTODOS DE TRANSFORMACIÓN")
    print(f"Clave de entrada (k): {clave} | Tamaño de tabla (M): {M}")
    print("=" * 60)

    # 1. División
    d_div = division(clave, M)
    print(f"1. División:              h({clave}) = {clave} % {M} -> {d_div}")

    # 2. Medio del Cuadrado (725934^2 = 526980172356 -> toma los 2 dígitos centrales '01')
    d_mc = medio_del_cuadrado(clave, M)
    print(f"2. Medio del Cuadrado:    h({clave}) -> {d_mc} (Cuadrado: {clave**2})")

    # 3.a Plegamiento Desplazado (partes de 2 dígitos: 72 + 59 + 34 = 165 % 100)
    d_pd = plegamiento_desplazado(clave, M)
    print(f"3.a Plegamiento Desplazado: h({clave}) -> {d_pd}")

    # 3.b Plegamiento Límite (72 + invierte(59->95) + 34 = 201 % 100)
    d_pl = plegamiento_limite(clave, M)
    print(f"3.b Plegamiento Límite:     h({clave}) -> {d_pl}")

    # 4. Extracción (por defecto toma los últimos dígitos para indexar hasta M-1)
    d_ext = extraccion(clave, M)
    print(f"4. Extracción:            h({clave}) -> {d_ext}")
    print("=" * 60)

