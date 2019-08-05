empleado_1 = float(input('Ingrese su sueldo:'))
empleado_2 = float(input('Ingrese su sueldo:'))
empleado_3 = float(input('Ingrese su sueldo:'))

def aumento():
    aumento_1 = empleado_1 + (empleado_1 * 0.10)
    aumento_2 = empleado_2 + (empleado_2 * 0.12)
    aumento_3 = empleado_3 + (empleado_3 * 0.15)
    print('El sueldo del primer empleado + 10% es:', aumento_1)
    print('El sueldo del segundo empleado + 12% es:', aumento_2)
    print('El sueldo del tercer empleado + 15% es:', aumento_3)


aumento()