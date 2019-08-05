def numeros_primos(numero):
    listado = list(range(2, numero + 1))

    for primo in listado:
        i = 0
        for num in listado:
            if num > primo and num % primo == 0:
                del listado[i]
            i += 1
    return listado

numero = int(input("Ingrese numero maximo: "))
print(numeros_primos(numero))