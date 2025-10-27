n = int(input())

valores = []

for i in range(1,n+1):
    if i % 2 == 0:
        valores.append(i)

for valor in valores:
    print(f"{valor}^2 = {valor**2}")