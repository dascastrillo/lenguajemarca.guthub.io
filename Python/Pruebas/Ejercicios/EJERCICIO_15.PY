print('¿Cual es tu nombre?')
nombre=( input())

sueldo=int( input("introduce el valor de sueldo"))
print(sueldo)

tipoEmpleado=str( input('Ingresa el valor de tipo de empleado(V, G, E o O)' ))
incremento=0

if tipoEmpleado == 'V':
    incremento = sueldo*0.10
    print('El incremento de V es: ' ,incremento)
    nuevosueldo=sueldo+incremento
    print("Nombre: ",nombre)
    print("incremento del sueldo de trabajador: ",incremento)
    print('Valor del nuevo salario: ', nuevosueldo)

elif tipoEmpleado == 'G':
    incremento = sueldo * 0.15
    nuevosueldo=sueldo+incremento
    print("Nombre: ",nombre)
    print("incremento del sueldo de trabajador: ",incremento)
    print('Valor del nuevo salario: ', nuevosueldo)
elif tipoEmpleado == 'E':
    incremento = sueldo * 0.20
    nuevosueldo=sueldo+incremento
    print("Nombre: ",nombre)
    print("incremento del sueldo de trabajador: ",incremento)
    print('Valor del nuevo salario: ', nuevosueldo)
elif tipoEmpleado == 'O':
    incremento = sueldo * 0.30
    nuevosueldo=sueldo+incremento
    print("Nombre: ",nombre)
    print("incremento del sueldo de trabajador: ",incremento)
    print('Valor del nuevo salario: ', nuevosueldo)
    
else:
    print('error al escribir...')