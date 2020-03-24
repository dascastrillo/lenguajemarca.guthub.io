import random

print('Adivina el Numero')
maquina=random.randint(1, 20)
usuario= int(input('Introduce un numero'))
while maquina < 6:
    maquina += 1
    suerte=random.randint(1,20)

    if suerte < usuario:
        print('Tu suerte es muy alta')
    if suerte > usuario:
        print('Tu suerte es muy baja')
    if suerte == usuario:
        break
if maquina == usuario:
    print('Has adivinado el numero.')
else:
    print('No has adivinado el numero.')