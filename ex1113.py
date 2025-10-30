import sys
xy = []
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        if a == b:
            break
        if a > b:
            xy.append("Decrescente")
        else:
            xy.append("Crescente")
    except EOFError:
        break
    
for i in range(len(xy)):
    print(xy[i])