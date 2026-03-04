"""

tipos de datos

int string float boolean

12312312341

hola

char caracter = 'a'

123123.345

True o False


tipos complejos
lista = [1, 2, 3, 4, 5]



a = 1
b = 2
c = 3

lista = [a, b, c] #puedes modificar los valores de detro
tuplas = (a, b, c)

lista = [1, 2, 3, 4, 5]
lista[0] = 43
lista = [43, 2, 3, 4, 5]

print("hola mundo")
variable = input("escribe tu variable")


# estructuras de control o flujo

variable = 2

if variable == 2:
    ejecutar codigo
elif variable == 3:
    ejecutar codigo


login
    usuario y contraseña

if usuario == correcto:
    ejecutar codigo
if contraseña == correcta:
    ejecutar codigo

    
formulario de contraseña
    contraseña con mas de 8 caracteres
    contraseña con 1 mayusctula como minimo
    contraseña con 1 número como minimo

if contraseña mayor a 8 caracteres:
    codigo
if contraseña 1
    codigo
if contraseña A
    codigo





menu de herramientas
1. borrar disco
2. copia de seguridad
3. salir del programa

if opcion == 1
    ...
elif opcion == 2
    ...
elif opcion == 3
    ...
else
    print("ERROR: no has seleccionado un numero entre el 1 y el 3")


    
switch:
    opcion 1:
        codigo
    opcion 2:
        codigo


        

# estructuras de repeticion
for ->  sí sabemos cuantas veces queremos ejecutar codigo
while ->NO sabemos cuantas veces queremos ejecutra codigo


for nombreVariable in range(3, 7) [3, 4, 5, 6]:


while(condicion sea verdadera):
    ejecutar codigo

    

## queremos contar del 1 al 10 pero en vez de 1 en 1 que sea de 2 en 2


"""

"""
ejercicio: recoger en una variable el input 
del usuario e imprimirla por pantalla.
    Si el nombre es literalmente 'ivan' se imprima por pantalla "hola profesor ivan"
    Si el nombre es literalmente 'safa' se imprima por pantalla "hola alumna safa"
    Si el nombre no es ninguno de los 2, mostrar por pantalla "no te conozoco"
"""


nombre_usuario = input("¿cual es tu nombre?")
print(nombre_usuario)

if nombre_usuario == "ivan":
    print("hola profe ivan")
elif nombre_usuario == "safa":
    print("hola alumna safa")
else:
    print("no te conozoco")




operacion_matematica = input("cuanto es 2+2")

if operacion_matematica == "4":
    print("todo perfecto")
elif operacion_matematica == "hola":
    print("no se puede escribir texto")
else:
    print("la operacion 2+2 es igual a 4, no es igual a", operacion_matematica, "no lo estas dicienod bien tienes qeu asistir a clase")

