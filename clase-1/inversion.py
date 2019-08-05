persona_1 = float(input('Ingrese el monto de su inversion: '))
persona_2 = float(input('Ingrese el monto de su inversion: '))
persona_3 = float(input('Ingrese el monto de su inversion: '))

total_inversion = persona_1 + persona_2 + persona_3

def empresa():
    p_1_inversion = (persona_1 * 100) / total_inversion
    p_2_inversion = (persona_2 * 100) / total_inversion
    p_3_inversion = (persona_3 * 100) / total_inversion
    print('El % que invirtio la persona 1 es: ', p_1_inversion)
    print('El % que invirtio la persona 2 es: ', p_2_inversion)
    print('El % que invirtio la persona 3 es: ', p_3_inversion)

empresa()