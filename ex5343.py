from collections import Counter

try:
    n = int(input())
    lista = []

    for _ in range(n):
        num = int(input())
        if 1 <= num <= 10**5:
            lista.append(num)

    contagens = Counter(lista)
    
    numeros_unicos = sum(1 for contagem in contagens.values() if contagem == 1)
    
    print(numeros_unicos)

except ValueError:
    pass
