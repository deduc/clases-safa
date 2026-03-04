# cond2.py

# aqui estamos declarando las variables, no estamos asignando su valor
a: int
b: int

# aqui estamos asignando los valores a nuestras variables declaradas
# estamos casteando (convertir el tipo de dato) a numero entero (int) el resultado de obtener el input del usuario
a=int(input('Valor 1: '))
b=int(input('Valor 2: '))

"""
existe una operacion llamada "to cast" o "cast" o "castear"
que significa convertir o intentar convertir una variable a un tipo de dato en concreto
"""
a = 11
b = 23
# si el numero a es par
if a%2==0:
    # si el numero b es par
    if b%2==0:
        print('SI')
    else:
        print('NO')
# si el numero a es impar
else:
    if b%2==0:
        cadena_de_texto = "NO, la variable a con valor"
        cadena_de_texto = cadena_de_texto + str(a)
        cadena_de_texto = cadena_de_texto + "es impar. y el valor del nuemro b"
        cadena_de_texto = cadena_de_texto + str(b)
        cadena_de_texto = cadena_de_texto + "es par"

        print(f"NO, la variable a con valor {a} es impar. y el valor del numero b {b} es par")
    else:
        print('SI')
