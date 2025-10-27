n = int(input())
medias = []
for i in range(n):
    a, b, c = map(float, input().split())
    media = (a * 2 + b * 3 + c * 5) / 10
    medias.append(f"{media:.1f}")

for i in medias:
    print(i)
