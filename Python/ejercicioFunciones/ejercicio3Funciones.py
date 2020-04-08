import sys
def menu():
    print('Supermercado')
    print('1. Cobrar siguiente carro')
    print('2.Cerrar la caja')
    opciones=input('elige una opcion: ')

    if opciones == '1':
        super()

    elif opciones == '2':
        exit

    else:
        print('no has introducido numero')
        opciones=input('introduce un numero: ')
    input('Intro cualquier teclado para finalizar')


def super():
    try: 
        print('SuPermercado')
        productos = 1  # contar producto 
        precioT = 0  # Acumulador de productos

        while productos <= 5:
            mensaje = "Ingresa el precio del producto número {}: ".format(productos)
            precio = input(mensaje) # Convertir a flotante
            precio = float(precio) # añado al precio total
            precioT = precioT + precio # leido el producto, le sumamos al contador
            productos = productos + 1 # Cuando el ciclo termine calculamos el IVA
        aumento = precioT * (0.21 / 100)  #sumar iva
        # Sumar el aumento
        iva = precioT + aumento
        # Imprimir totales
        print("Total: ${}".format(precioT))
        print("IVA: ${}".format(aumento))
        print("Total con IVA: ${}".format(iva))
    except:
        print("Vaya!",sys.exc_info()[0],"ocurrio.")
        print("Entrada siguiente")
        print()
menu()

