
n = int(input())
numbers = []

for _ in range(n):
    num = int(input())
        

    if (num == 0):
        numbers.pop()
    else:
        numbers.append(num)
        
sums = sum(numbers)

print("\n" + sums + "\n")
