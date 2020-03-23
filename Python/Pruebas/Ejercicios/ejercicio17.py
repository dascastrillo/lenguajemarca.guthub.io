invitados=int( input("Numeros de invitados: "))
invitados
precioniño=15

if invitados>=1 and invitados<=10:
    invitados=200
    print(invitados, '€')
elif invitados>=10 and invitados<=20:
    invitados=320
    print(invitados, '€')

elif invitados>20:
    niño=int( input("Numeros de niños:"))
    invitados=niño*precioniño
    print(invitados, '€')
else:
    print('error al introducir numeros...')

duracion=int(input('La duracion es: '))
if duracion >=1 and duracion<=3:
    precio=100
elif duracion >=4 and duracion <=6:
    precio=150
elif duracion >=6:
    precio=200
else:
    print('error de numero...')

total=invitados+precio
print('El precio a pagar es de: ', total ,'€')
