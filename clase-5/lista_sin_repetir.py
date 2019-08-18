k = int(input())
lista = map(int, input().split())

n1 = 0
n2 = 0

def numerosQueSumanK(lista, k):
    for i in lista:
        for j in lista:
            print(f"i: {i} --- j: {j}")
            if i == j:
                continue
            if i + k == j:
                n1 = i
                n2 = j
                break
    if n1 + n2 != k:
        print("no se puede sumar k")
            
    print(n1, n2)
   
            


(numerosQueSumanK(lista, k))