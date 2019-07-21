""" def contar_letras(palabra, letra):
    n = 0
    r = 0
    while n < len(palabra):
        if palabra[n] == letra:
            r += 1
        n +=1
    return r   
 """
def reemplazar(palabra, letra, letra_nueva):
     n = 0
     palabra_final = ""

     while n < len(palabra):
        if palabra[n] == letra:
             palabra_final = palabra_final + letra_nueva
        else:
            palabra_final = palabra_final + palabra[n]
        n += 1
     return palabra_final

palabra = input('ingresa algo: ')
palabra  = reemplazar(palabra, 'a', 'c')
print(palabra)