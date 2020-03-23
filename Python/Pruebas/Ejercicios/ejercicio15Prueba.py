import os

nombre = input ('Ingrese el nombre: ')
sueldo = float (input ('Ingrese el valor de sueldo: '))
tipo_de_empleado = float (input ('Ingrese el valor de tipo de empleado: '))
incremento=0
if tipo_de_empleado==1:
    incremento=sueldo*0.05
if tipo_de_empleado==2:
    incremento=sueldo*0.07
if tipo_de_empleado==3:
    incremento=sueldo*0.09
if tipo_de_empleado==4:
    incremento=sueldo*0.12
if tipo_de_empleado==5:
    incremento=sueldo*0.15
nuevo_salario=sueldo+incremento
print ('Nombre: ' + nombre)
print ('Valor de incremento: ' + repr (incremento))
print ('Valor de nuevo salario: ' + repr (nuevo_salario))
print ()
os.system ('pause')