n = int(input())

inc = 0
outc = 0

for i in range(n):
    s = int(input())

    if 10 <= s <= 20:
        inc+=1
    else:
        outc+=1

print(f"{inc} in\n{outc} out")