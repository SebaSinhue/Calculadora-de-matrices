import numpy

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el elemento [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    return numpy.add(matriz1, matriz2)

def restar_matrices(matriz1, matriz2):
    return numpy.subtract(matriz1, matriz2)

def multiplicar_matrices(matriz1, matriz2):
    return numpy.dot(matriz1, matriz2)

def gauss_jordan(matriz):
    matriz = numpy.array(matriz)
    filas, columnas = matriz.shape

    for i in range(filas):
        pivote = matriz[i][i]
        if pivote == 0:
            raise ValueError("El pivote no puede ser cero. No se puede aplicar Gauss-Jordan.")

        matriz[i] = matriz[i] / pivote

        for j in range(filas):
            if j != i:
                multiplicador = matriz[j][i]
                matriz[j] = matriz[j] - multiplicador * matriz[i]

    return matriz

filas = int(input("Ingrese el numero de filas de las matrices: "))
columnas = int(input("Ingrese el numero de columnas de las matrices: "))

print("Ingrese los elementos de la primera matriz:")
matriz1 = crear_matriz(filas, columnas)

print("Ingrese los elementos de la segunda matriz:")
matriz2 = crear_matriz(filas, columnas)

resultado_suma = sumar_matrices(matriz1, matriz2)
resultado_resta = restar_matrices(matriz1, matriz2)
resultado_multiplicacion = multiplicar_matrices(matriz1, matriz2)

print("La suma de las matrices es:")
print(resultado_suma)

print("La resta de las matrices es:")
print(resultado_resta)

print("La multiplicación de las matrices es:")
print(resultado_multiplicacion)

print("Aplicando Gauss-Jordan a la matriz 1:")
matriz_gauss1 = gauss_jordan(matriz1)
print(matriz_gauss1)

print("Aplicando Gauss-Jordan a la matriz 2:")
matriz_gauss2 = gauss_jordan(matriz2)
print(matriz_gauss2)