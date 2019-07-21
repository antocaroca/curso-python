presion = int(input('Ingrese la presión del neumático: '))

volumen = int(input('Ingrese el volúmen: '))

temperatura = int(input('Ingrese la temperatura: '))

masa = (presion * volumen)/(0.37 * (temperatura + 460))

print('la masa del neumático es', masa)