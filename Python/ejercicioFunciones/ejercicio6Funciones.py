import os
def area_rectangulo():
    print("Introduce la base : ")
    base=pedirNumeroEntero()
    print("Introduce la altura : ")
    altura=pedirNumeroEntero()
    area_rectangulo=base*altura
    print("El area de un Rectangulo es : ",area_rectangulo) 

    input("Presione una tecla para continuar...")

def pedirNumeroEntero():
     
    while True:
        try:
            num = int(input())
            break
        except ValueError:
            print('Error, al introducir los datos')
            print ("Intentalo de nuevo") 
    return num

def area_circulo():
    pi=3.14159265359
    print('introduce el numero del radio: ')
    radio=pedirNumerosReales()
    r= pi * (radio ** 2)
    print('El area del Circulo es: ', r)

    input('Presiona cualquier tecla para continuar...')

def pedirNumerosReales():

    while True:
        try:
            NumReal = float(input())
            break
        except ValueError:
            print('Error al introducir numero')
            print('Vuelve a introducir numero ')
    return NumReal

def VolClindro():
    pi=3.14159265359
    print('introduce el valor de radio: ')
    r=pedirNumerosReales() #radio
    print(('introduce la altura: '))
    h=pedirNumerosReales() #altura
    Volumen= pi * (r ** 2) * (h)
    print('El volumen del cilindro es: ', Volumen)
    
    input('Presiona cualquier tecla para continuar...')

def ElevaPotencia():
    print('introduce la base: ')
    base=pedirNumerosReales()
    print('introduce el exponenete: ')
    exponente= pedirNumerosReales()
    resultado= base ** exponente
    print('El resultado es: ', resultado)

    input('Presiona cualquier tecla para continuar...')

while True:
    #borrar la pantalla Para DOS/Windows
    os.system ("cls") 
    print ("1. Calcular el area del rectangulo")
    # Area Circulo= π r²
    print ("2. Calcular el Area de un circulo")
    # debe calcule el volumen de un cilindro usando el dato que 
    # le devuelva la funcion del Area de Circulo.
     # Volumen Cilindro = π r² h
    print ("3. Calcular el Volumen de un Cilindro")
    print ("4. Elevar un número a una potencia ")
    print ("5. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
    
    if opcion == 1:
        area_rectangulo()
    elif opcion == 2:
        area_circulo()
    elif opcion == 3:
        VolClindro()
    elif opcion == 4:
        ElevaPotencia()
    elif opcion == 5:
        break
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin del Programa")
