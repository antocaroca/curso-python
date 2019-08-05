salario = float(input('Ingrese su salario anterior:'))
incremento = 0.25

def incremento_salario():
    aumento = salario * incremento
    salario_final = salario + aumento
    print('su salario mas incremento del 25% es:', salario_final)


incremento_salario()