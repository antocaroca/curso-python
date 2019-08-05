producto = float(input('Ingrese el valor del producto:'))
iva = 0.13

def calculo_iva():
    precio_con_iva = producto + (producto * iva)
    print('EL precio final del producto con iva es:', precio_con_iva)

calculo_iva()