numero=int(input('introduce un numero: '))
primo=True

for i in range(2,numero):
    if numero % i == 0:
        primo=False
    
if primo:
    print('El numero introducido es primo.')
else:
    print('El numero introducido no es primo.')
