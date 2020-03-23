import os
respuesta='S'
#Metodo que limpia la pantalla y muestra el menu nuevamente.
def menu():
    '..MENU..'
os.system('cls') #si es linux se usa clear
print('Selecciona una opacion')
print('\t1. comenzar programa')
print('\t2. imprimir listado')
print('\t3. finalizar programa')

while respuesta=='S':
    menu()
    opcion=input('Introduce un numero:')
    
    if opcion=='1':
        print('Esto es un texto')
        input('estas en la opcion 1...\npulsa una tecla para continuar ')
    elif opcion=='2':
        print('esto es un texto')
        input('Estas en la opcion 2...\npulsa para continuar')
    elif opcion=='3':
        break
    else:
        print('No esta la opcion')
    