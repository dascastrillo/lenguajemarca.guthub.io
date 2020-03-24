import random

#inicializo las variables
intento= random.randint (1, 10)
suerte=random.randint(1,10)
numero=random.randint(1,10)

#En ese ejercicio no necesito utilizar el bucle while, ademas no hara nada
while intento < 6:
    intento +=1
    if intento == suerte:
        break
#uso la condicion if para comprar si los dos numeros son iguales
if intento ==  numero:
    print('el numero:', intento, 'y ', numero, 'Son iguales.')
else:
    print('el numero:', intento, 'y ', numero, 'no son iguales.')
input('Presion INTRO para salir del programa') #finalizo programa
    