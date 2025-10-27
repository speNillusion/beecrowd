def resolver():
    while True:
        try:
            linha_n = input()
            if not linha_n:
                break
            n = int(linha_n)
            
            pontos = []
            for _ in range(n):
                x, y = map(int, input().split())
                pontos.append((x, y))

            pontos.sort()

            acima = {}
            abaixo = {}
            max_pontos = 0

            for i in range(n):
                xi, yi = pontos[i]
                
                melhor_acima = 0
                melhor_abaixo = 0

                for j in range(i):
                    xj, yj = pontos[j]
                    
                    if yi == yj + 2:
                        melhor_acima = max(melhor_acima, abaixo.get(j, 0))
                    
                    if yi == yj - 2:
                        melhor_abaixo = max(melhor_abaixo, acima.get(j, 0))

                acima[i] = melhor_acima + 1
                abaixo[i] = melhor_abaixo + 1
                
                max_pontos = max(max_pontos, acima[i], abaixo[i])

            print(max_pontos)

        except (EOFError, ValueError):
            break

resolver()
