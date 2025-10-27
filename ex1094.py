coelhos = 0
ratos = 0
sapos = 0
t = int(input())

for i in range(t):
    caso = input().split()
    if caso[1] == "C":
        coelhos = coelhos + int(caso[0])
    elif caso[1] == "R":
        ratos = ratos + int(caso[0])
    elif caso[1] == "S":
        sapos = sapos + int(caso[0])

total_cobaias = coelhos + ratos + sapos

percentual_coelhos = (coelhos / total_cobaias) * 100
percentual_ratos = (ratos / total_cobaias) * 100
percentual_sapos = (sapos / total_cobaias) * 100

print("Total: %d cobaias" % total_cobaias)
print("Total de coelhos: %d" % coelhos)
print("Total de ratos: %d" % ratos)
print("Total de sapos: %d" % sapos)
print("Percentual de coelhos: %.2f %%" % percentual_coelhos)
print("Percentual de ratos: %.2f %%" % percentual_ratos)
print("Percentual de sapos: %.2f %%" % percentual_sapos)