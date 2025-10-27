dicCdd, T = {}, 0
def floor(x): return int(x) if x == int(x) and x > 0 else int(x) -1
while True:
    N = int(input())
    totalX, totalY, consumos, i, output = 0, 0, {}, 0, []
    if N == 0: break
    if T: print("")
    while i < N:
        X, Y = map(int, input().split(' '))
        totalX += X
        totalY += Y
        if Y//X in consumos: consumos[Y//X] += X
        else: consumos[Y//X] = X
        i += 1
    consumo_total = ((100 * totalY)/totalX)/100
    consumo_medio = floor(consumo_total*100)/100
    keys = sorted(list(consumos.keys()))
    for key in keys: output.append(f'{consumos[key]}-{key}')
    T += 1
    entrada = {"cidade": T,"consumo_total": f'{" ".join(output)}',"consumo_medio": f'{consumo_medio:.2f} m3.'}
    dicCdd[T] = entrada
for entrada in dicCdd.values(): print(f'Cidade #{entrada["cidade"]}:\n{entrada["consumo_total"]}\nConsumo medio: {entrada["consumo_medio"]}')