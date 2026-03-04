"""
cuenta cuales son los numeros comprendidos entre 1 y 10
"""

primerNumero = 1
ultimoNumero = 10
for numero in range(primerNumero, ultimoNumero+1):
    print(numero)


"""
cuenta los numeros de 2 en 2 hasta el 10, comenzando por el numero 0
"""
for n in range(0, 10+1, 2):
    print(n)


"""
queremos contar los numeros que hay entre el 0 y el 100 saltando de 3 en 3

pero queremos imprimir solo los numeros pares en cada iteracion
"""

for n in range(0, 100+1, 3):
    if (n % 2) == 0:
        print(n)