n = int(input())

menor_valor_por_grama = float('inf')

for i in range(n):
    preco, gramas = input().split()
    preco = float(preco)
    gramas = int(gramas)

    valor_por_grama_atual = preco / gramas
    
    if valor_por_grama_atual < menor_valor_por_grama:
        menor_valor_por_grama = valor_por_grama_atual

custo_final = menor_valor_por_grama * 1000

print(f"{custo_final:.2f}")
