import sys
import math
dicCdd, T = {}, 0
while True:
    try:
        line = sys.stdin.readline()
        if not line.strip(): break
        N = int(line)
    except (IOError, ValueError):
        break    
    if N == 0: break
    totalX, totalY, consumos, i, output = 0, 0, {}, 0, []
    if T: print("")
    while i < N:
        try:
            line = sys.stdin.readline()
            if not line.strip(): break
            X, Y = map(int, line.split(' '))
        except (IOError, ValueError):
            break
        totalX += X
        totalY += Y
        if Y//X in consumos: consumos[Y//X] += X 
        else: consumos[Y//X] = X
        i += 1
    consumo_total = ((100 * totalY)/totalX)/100
    consumo_medio = math.floor(consumo_total*100)/100
    keys = sorted(list(consumos.keys()))
    for key in keys: output.append(f'{consumos[key]}-{key}')
    T += 1
    entrada = {"cidade": T,"consumo_total": f'{" ".join(output)}',"consumo_medio": f'{consumo_medio:.2f} m3.'}
    dicCdd[T] = entrada
for entrada in dicCdd.values(): 
    print(f'Cidade# {entrada["cidade"]}:')
    print(f'{entrada["consumo_total"]}')
    print(f'Consumo medio: {entrada["consumo_medio"]}')
    print("\n")
