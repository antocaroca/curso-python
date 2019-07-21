calificacion_parcial_1 = int(input('Ingrese la calificación parcial número 1: '))
calificacion_parcial_2 = int(input('Ingrese la calificación parcial número 2: '))
calificacion_parcial_3 = int(input('Ingrese la calificación parcial número 3: '))

examen_final = int(input('Ingrese la calificación de su examen final: '))
trabajo_final = int(input('Ingrese la calificación de su trabajo final: '))

promedio_3_calificaciones_parciales = ((calificacion_parcial_1 + calificacion_parcial_2 + calificacion_parcial_3) / 3) * 0.55

examen_final = examen_final * 0.30

trabajo_final = trabajo_final * 0.15

calificacion_final = promedio_3_calificaciones_parciales + examen_final + trabajo_final

print('Tu calificación final en Algoritmos es:', calificacion_final)