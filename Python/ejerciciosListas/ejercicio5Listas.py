import string
try:
    def Calcular_leta_DNI():
        lista = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        dni =input("Introduzca el DNI(con letra): ")
        respuesta= "No ha introducido un DNI valido"
        if (len(dni) == 9):
            letra = dni[8].upper()
            dni = dni[:8]
            if ( len(dni) == len( [n for n in dni if n in numeros] ) ):
                if lista[int(dni)%23] == letra:
                    respuesta="El DNI introducido es correcto"
        print(respuesta)
except:
    print('Error, ha ocurrido algo imprevisto')
    print('Vuelve a intentarlo')

Calcular_leta_DNI()