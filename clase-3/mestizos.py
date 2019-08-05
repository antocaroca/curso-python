"""
mestizos(raza1, raza2, archivoPerros,archivoNombres) la cual recibe como parámetros 2 razas distintas, 
luego el nombre del archivo de César y por último un
nombre de archivo donde se escribirá. 
La función debe escribir en el archivo archivoNombres los nombres de los perros que
pertenecen a ambas razas, si ningún perro pertenece a ambas razas a la vez, debe escribir Ninguno.
"""
razas={}
archivo = ("perritos.txt", "mestizos.txt")
def mestizos(raza1, raza2, archivoPerros,archivoNombres):
    for linea in archivo:
        fecha, nombre, raza, prob, sol = linea.strip().split(";")

        if raza == raza1 and raza == raza2:
            archivo = open("mestizos.txt", "w")
            for nombre in archivo.items():
                archivo.write(nombre + "\n")
                

        
    archivo.close()
    return razas



mestizos("salchica", "pastor aleman", "perritos.txt", "mestizos.txt")
