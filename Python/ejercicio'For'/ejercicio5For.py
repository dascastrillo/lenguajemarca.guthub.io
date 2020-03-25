suma=0
# se ejecuta 10 veces 
for numero in range(10):
    numero2=int (input('introduce el numero: '))
    #cojo los ultimos 5 numero de los 10 y lo suma.
    if numero > 4:
        suma=suma + numero2
#sale del bucle para que me de el resultado de la suma de los 5 ultimos numeros.
print(suma)
input('Pulsa INTRO para finalizar ')
