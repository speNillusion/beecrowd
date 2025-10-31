vermelhas = 5
azuis = 3
verdes = 2
totalBolas = vermelhas + azuis + verdes
print(f"Probabilidade de escolher duas bolas com a mesma cor: {((vermelhas / totalBolas) * ((vermelhas - 1) / (totalBolas - 1)) + (azuis / totalBolas) * ((azuis - 1) / (totalBolas - 1)) + (verdes / totalBolas) * ((verdes - 1) / (totalBolas - 1))):.7f}")
