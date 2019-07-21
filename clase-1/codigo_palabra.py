def codigo_palabra(codigo):
    resultado = ""
    pos = len(codigo)

    while pos >= 0:
        if (pos + 1) % 2 != 0:
            resultado += codigo[pos]

        pos -= 1
    return resultado

print(codigo_palabra("aczaarltp"))
print(codigo_palabra("axruatgrrreov"))




