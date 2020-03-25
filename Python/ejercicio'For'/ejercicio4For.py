#genera 10 numero, positivos y negativos.
for i in range(-5, 5):
    if i > 0:  #numeros positivos
        print('El numero ', i, ' es positivo')
    elif i < 0: # numeros negativos
        print('El numero', i, ' es negativo')
    elif i == 0: # soluciono un error, si es 0 que sea positivo.
        print('El numero', i, ' es positivo')
    else:
        #y si no es ninguna de las anteriores que me muestre el mensaje.
        print('no has introducido un numero')
input('Introduce INTRO para finalizar...')