count = 0
media = 0
for i in range(6):
    n = float(input())

    if n >=1:
        count+=1
        media+=n

media = media / count

print(f"{count} valores positivos\n{media:.1f}")
