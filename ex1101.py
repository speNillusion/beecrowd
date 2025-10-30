import sys
xy = []
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        if a <= 0 or b <= 0:
            break
        if a > b:
            a, b = b, a
        temp_xy = ""
        temp_sum = 0
        for i in range(a, b+1):
            temp_sum += i
            temp_xy += f"{i} "
        xy.append(f"{temp_xy}Sum={temp_sum}")
    except EOFError:
        break
    
for i in range(len(xy)):
    print(xy[i])

