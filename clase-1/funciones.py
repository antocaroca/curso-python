def par(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = int(input("ingrese un numero: "))
print("el numero", numero, "es", par(numero))

