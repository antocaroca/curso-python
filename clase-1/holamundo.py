# export PYTHONIOENCODING=utf-8
nombre = input('para continuar ingrese su nombre: ')
print("Hola", nombre + '!')
print('por favor ingrese los siguientes datos a continuación: ')

edad = int(input('edad: '))
estatura = float(input("estatura (metros): "))
relleno = bool(input("no ingreses nada: "))

print('\n', end='')

print('resumen de', nombre + ':')
print()
print("\tEdad:", edad)
print("\tAño de nacimiento:", 2019 - edad)
print("\tEstatura:", estatura, "[m]")
print("\tRellenó el último campo?:", relleno)

