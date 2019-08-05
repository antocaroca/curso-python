# export LC_CTYPE=en_US.UTF-8
archivo = open("notasMatematicas.txt", "r")
notas = {}

# for linea in archivo:
#     print("linea original:", linea)
#     print(linea.strip().split())

for linea in archivo:
    nombre, nota = linea.strip().split()
    notas[nombre] = nota


archivo.close()
print(notas["Gonzalo"])