numero = int(input('Ingrese un número: '))

if numero % 2 == 0:
    print(numero, 'es par')
else:
    if numero == 3: # se ejecuta este if solo si se cumple esta condición
        print('es 3')
    print(numero, 'es impar')


