import time
import os
lista=[]
try:
    def menu():
        os.system ("cls")  
        print("Situación epidemiológica del coronavirus (COVID-19) en Castilla y León ")
        print ("Actualización diaria. Datos a ",time.strftime("%d/%m/%y"))
        print("\t1.- Dar de alta  Provincia y datos (confirmados y nuevos)")
        print("\t2.- Introduce una provincia para modificar sus datos(confirmados y nuevos) " )
        print("\t3.- Numero Total de casos Confirmados y Nuevos en la Comunidad ")
        print("\t4.- Listado de la situacion  general por provincias(confirmados y nuevos)")
        print("\t5.-Salir")

        op=int(input('Elije la opcion: '))

        if op == 1:
            añadir()
        elif op == 2:
            print()
        elif op == 3:
            mostrar()
        elif op == 4:
            general()
        elif op == 5:
            exit
        
    
except ValueError:
    print("No pude convertir el dato a un entero.")
except Exception as e: # OJO SIEMPRE LA ULTIMA
    print("Ha ocurrido un error no previsto del tipo ", type(e).__name__ )

def añadir():
    
    numeroveces=int
    provincia=str(input('introduce el nombre de la provincia: '))
    lista.append(provincia)
    casos=int(input('introduce los numeros de casos confirmados: '))
    lista.append(casos)
    nuevoscasos=int(input('introduce el numero de nuevos casos positivos: '))
    lista.append(nuevoscasos)
    menu()

def mostrar():
    print('Casos confirmados: ', lista[1])
    print('Casos confirmados positivos: ', lista[2])

    input('')
    menu()

def general():
    print('General')
    print('Provincias: ', lista[0])
    print('Casos confirmados: ', lista[1])
    print('Nuevos casos positivos: ', lista[2])
    input('')
    menu()

menu()

