import math
c=float(input("cantidad de euros: "))
x=float( input("el porcentaje de interes:"))
anos=float( input("introduce el numero de años"))
#math.pow (base,exponente)
cn=(c)*math.pow((1+(x/100)), anos)
print("El capital final es:", cn)

