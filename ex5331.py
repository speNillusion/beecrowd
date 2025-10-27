n = int(input())
fib = [0,1]

for _ in range(n):
    fib.append(fib[-1]+fib[-2])

print(fib[n-1])