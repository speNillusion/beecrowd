import sys
xy = []
while True:
    try:
        x, y = map(int, sys.stdin.readline().split())
        if x == 0 or y == 0:
            break
        if x > 0 and y > 0:
            xy.append("primeiro")
        elif x < 0 and y > 0:
            xy.append("segundo")
        elif x < 0 and y < 0:
            xy.append("terceiro")
        elif x > 0 and y < 0:
            xy.append("quarto")
    except EOFError:
        break

for i in range(len(xy)):
    print(xy[i])