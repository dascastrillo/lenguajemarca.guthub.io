total=0
precio=float(input("Precio de una producto: $"))
while precio!=0:
    if precio<0:
        print("Precio no válido.")
    else:
        total=total+precio
    precio=float(input("Precio de una producto: $"))
if total>1000:
    total=total-(total*0.1)
print("Precio total a pagar: $", total)