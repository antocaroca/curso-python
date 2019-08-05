ginecologia = 0.40
traumatologia = 0.30
pediatria = 0.30

presupuesto = int(input('Ingrese el presupuesto anual:'))

def hospital():
    presupuesto_ginecologia = presupuesto * ginecologia
    presupuesto_traumatologia = presupuesto * traumatologia
    presupuesto_pediatria = presupuesto * pediatria
    print('El presupuesto para ginecologia es:', presupuesto_ginecologia)
    print('El presupuesto para traumatologia es:', presupuesto_traumatologia)
    print('El presupuesto para pediatria es:', presupuesto_pediatria)

hospital()