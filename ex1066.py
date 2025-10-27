pares = 0
impares = 0
positivos = 0
negativos = 0

for _ in range(5):
    n = int(input())

    if n % 2 == 0:
        pares+=1
    else:
        impares+=1

    if n >= 1:
        positivos+=1
    if n < 1:
        negativos+=1
    

print(f"{pares} valor(es) par(es)\n{impares} valor(es) impar(es)\n{positivos} valor(es) positivo(s)\n{negativos-1} valor(es) negativo(s)")
