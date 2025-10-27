n = int(input())
ant = -1
count = 0

for i in range(n):
    num = int(input())

    if num != ant:
        count+=1
    
    ant = num

print(count)
