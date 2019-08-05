
nombre = input('Ingrese el nombre del trabajador:')
horas = float(input('Ingrese las horas trabajadas:'))
precio_por_hora = float(input('Ingrese el precio por hora de trabajo:'))
impuesto = 0.10

def calculo_sueldo():
    sueldo_bruto = horas * precio_por_hora
    descuento = sueldo_bruto * impuesto
    salario_a_pagar = sueldo_bruto - descuento
    print('\t Trabajador:', nombre)
    print('\t Sueldo bruto:', sueldo_bruto)
    print('\t Descuento de renta:', descuento)
    print('\t Salario a pagar:', salario_a_pagar)

calculo_sueldo()