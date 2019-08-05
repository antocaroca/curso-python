lunes = float(input('Ingrese el tiempo en minutos del dia lunes: '))
martes = float(input('Ingrese el tiempo en minutos del dia martes: '))
miercoles = float(input('Ingrese el tiempo en minutos del dia miercoles: '))

def cronometro():
    tiempo_promedio = (lunes + martes + miercoles) / 3
    print('El tiempo promedio en minutos es:', tiempo_promedio)

cronometro()