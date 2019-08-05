notas = {}
archivosNotas = ("notasMatematicas.txt", "notasCalculo.txt")

def leerNotas(nombreArchivo):
	archivo = open(nombreArchivo, "r")

	for linea in archivo:
		nombre, nota = linea.strip().split()
		if nombre not in notas:
			notas[nombre] = []
		notas[nombre].append(int(nota))

	archivo.close()

for archivoNotas in archivosNotas:
	leerNotas(archivoNotas)


archivo = open("promedios.txt", "w")
for nombre, listaNotas in notas.items():
	promedio = sum(listaNotas) / len(listaNotas)
	archivo.write(nombre + " " + str(promedio) + "\n")

archivo.close()