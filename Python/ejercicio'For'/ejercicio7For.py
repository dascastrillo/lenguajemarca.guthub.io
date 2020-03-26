
totale=0
totali=0
totales=0

triangulo=int(input('ingresa el numero de triangulo: ')  #cuantas veces quiero repetir el proceso
for i in range(triangulo):

    a=int( input('ingresa el valor a: '))
    b=int( input('ingresa el valor b: '))
    c=int( input('ingresa el valor c: '))
    #si los valores son iguales imprime el mensaje y guardo en una variable
    if a == b and b == c: 
        print('Es triangulu equilatero')
        totale += 1
    # uno es igual y los tros dos no, imprime el mensaje y lo guardo en otra variable.
    elif a == c and a != b and c != b: 
        print('Es tringualo isósceles')
        totali += 1
    #y si son distintos imprimes el mensaje y guardo la informacion en una variable.
    elif a != b and a != c and b != c: 
        print('Es triangulo escaleno')
        totales += 1
#informacion de los triangulos.
print(totale)
print(totales)
print(totali)