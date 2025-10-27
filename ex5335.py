n = int(input())

count = 0

if 1<=n<=100:
    for i in range(n):
        if i % 3 == 0:
            count+=1

print(count-1)