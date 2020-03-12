 # 4 personas --> 1/2kg arroz 1/4 kg gambas
 # por pantalla el numero de comensales, le precio de kilo de los ingredientes.

arroz=1,52
gambas=13,50
cigalas=82
calamares=20
almejas=20
pimientos=2,25
cebollas=1,35
ajos=6,95
tomates=1,25
paella ={
    'ingredientes': ['arroz','gamba','caldo de pescado','cigalas medianas','calamares','almeja','pimiento rojo','cebolla','tomate', 'ajo', 'aceite de oliva', 'sal'],
    'precio': ['arroz 1kg = 1.52€', 'gamba arrocera 1kg = 13,50€','1kg cigalas gallegas grandes = 82€', '1kg calamares grandes = 20€', '1kg almeja mediana = 20€', '1kg pimiento rojo = 2,25€', '1kg cebollas grandes = 1.35€', '1kg ajo morado= 6,95€', '1kg tomate frito = 1,25€']

}


#orden
persona=int( input("numero de personas: "))
print("Los ingredientes son: ")
for ingre in paella ['ingredientes']:
    print('\t', ingre)

print('Los precios por kilos son: ')
for precio in paella ['precio']:
    print('\t', precio)

resultado = 1.52+13.50+82+20+20+2.25+1.35+6.95+1.25
print('el coste de todos los ingredientes son: ',resultado,'€')