n = int(input())
from collections import Counter
botas = []
pares = 0
ant = ""

for i in range(n):
    bota = input()
    botas.append(bota.replace(" ", ""))

a = Counter(botas)

for q in a.values():
    if q > 1:
        pares+=1

print(pares)
    