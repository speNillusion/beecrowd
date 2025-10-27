n = int(input())
pares = -1
for i in range(n+1):
    if 1<=n<=100:
        if i % 2 == 0:
            pares+=1

print(pares)