#Escribir dos funciones que permitan calcular:
#   o	La cantidad de segundos en un tiempo dado en horas, minutos y segundos.##
#   o	La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
#Haz un menú para poder elegir una de las 2 opciones
import sys

def menu():
    print('CALCULADORA DE TIEMPO')
    print('1. Ver la cantidad de segundos de un tiempo dado')
    print('2. ver la cantidad de horas y segundos de un tiempo dado')
    print('3. salir')
    opcion=input('Elige una opcion: ')
    try: 
        if opcion == '1' :
            opcion1()
        elif opcion == '2':
            Segundos()
        elif opcion == '3':
            exit
        else:
            print('No has introducido un numero')
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()

def Segundos():
    Segundos=float (input('introduce un cantidad de segundos: ')) #introdcucir valor
    m= Segundos / 60 #calcular minutos
    h= Segundos * (1/60) * (1/60) #clacular horas
    print(Segundos, 'segundos son: ', m, 'minuto', 'y', h, 'hora/horas')
    exit
def opcion1():
    segundos=float (input ('introduce una cantidad de numero de segundos: '))
    s= segundos % 60 # calcular segundos
    m= (segundos // 60) % 60 # calcular minutos
    h= (segundos // 60) // 60  # calcular horas
    print ('Segundos: ', h, 'h. ', m, 'min. ', s, 's. ')
    exit


menu() #imprimir pantalla del resultado.
