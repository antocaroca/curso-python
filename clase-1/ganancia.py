articulo = int(input('Ingrese el valor del articulo:'))
ganancia = 0.30

def ganancia_30():
    precio_venta = articulo + (articulo * ganancia)
    print('Para obtener una ganancia del 30% debe vender el articulo a: ', precio_venta)

ganancia_30()

