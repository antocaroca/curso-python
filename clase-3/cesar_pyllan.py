razas = {}
def leer_razas(archivoPerros):
   
    archivo = open(archivoPerros, "r")

    for linea in archivo:
        fecha, nombre, raza, prob, sol = linea.strip().split(";")

        if raza not in razas:
            razas[raza] = []
        razas[raza].append(nombre)
        
    archivo.close()
    return razas

# razas = print(leer_razas("perritos.txt"))

def mestizos(raza1, raza2, nombrePerritos, nombreArchivo):
    razas = leer_razas(nombrePerritos)
    archivo = open(nombreArchivo, "w")

    for perro in razas[raza1]:
        if perro in razas[raza2]:
            archivo.write(perro + "\n")

    archivo.close()

mestizos("salchicha", "san bernardo", "perritos.txt", "mestizos.txt")