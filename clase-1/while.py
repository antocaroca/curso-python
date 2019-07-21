# conjetura de collatz
# https://www.youtube.com/watch?v=HpcYW08Ug7g

numero = int(input('Ingrese un número: '))

while numero != 1:
    if numero % 2== 0:
        numero /= 2    
    else:
        numero = numero*3+1
    print(numero)
       
   