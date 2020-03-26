base=float(input('introduce base: '))
exponente=int(input('introduce exponente: '))
potencia=int
for i in range(exponente):
    potencia= 1
    exponente= i
    
    for j in range(exponente):
        potencia *= base

print(base, '^', i, '=', potencia)