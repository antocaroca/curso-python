age = int(input('Ingrese su edad: '))

def pulsaciones():
    num_pulsaciones = (220 - age) / 10
    print('El numero de pulsaciones cada 10 segundos de ejercicio es:', num_pulsaciones)


pulsaciones()