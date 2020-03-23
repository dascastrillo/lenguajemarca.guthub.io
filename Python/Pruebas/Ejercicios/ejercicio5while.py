lista={}
respuesta='S'
while respuesta=='S':
    elemento=input('introduce un producto')
    precio=float(input('introduce el precio de ' +elemento +":"))

    lista[elemento]=precio
    respuesta=input('¿quieres añadir mas elementos a la lista (S/N)?')
    coste=0
    print('lista de la compra')

    if coste > 1000:
        coste=precio*0.10/100
        print('coste total + descuento(10%)', coste)
    else:
        print('se ha producido un error')
        elemento=input('')
    
        for elemento, precio in lista.items():
            print(elemento, "\t", precio)
        coste +=precio
        print('coste total: ', coste)
