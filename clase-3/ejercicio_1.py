numero = int(input('Ingrese un numero: '))

archivo = open("numeros.txt", "w")

# contador = 0
# while contador <= numero:
#     archivo.write(str(contador))
#     contador += 1  

# for i in range(0, numero + 1):
#     archivo.write(str(i))

for i in range(0, numero +1):
    if i < numero:
        archivo.write(str(i)+"\n")
    else:
        archivo.write(str(i))

archivo.close()