def eratostenes(n):
    criba = (n+1)*[True]
    i = 2
    while i ** 2 <= n:
        if criba[i]:
            j = 2
            while i * j <= n:
                criba[i * j] = False
                j += 1
        i += 1
    primos = []
    i = 2
    while i <= n:
        if criba[i]:
            primos.append(i)
        i += 1
    return primos
n = int(input('ingrese n: '))
print(eratostenes(n))
