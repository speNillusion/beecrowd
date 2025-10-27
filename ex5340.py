linhas, colunas = map(int, input().split())

somatotal = 0

for i in range(linhas):

    colunaatual = list(map(int, input().split()))

    for n in colunaatual:
        somatotal+=n


print(somatotal)