operation = input()
matrix = []

for _ in range(12):
    row = []
    for _ in range(12):
        row.append(float(input()))
    matrix.append(row)

sum_elements = 0.0
count_elements = 0

for i in range(12):
    for j in range(12):
        if j < i:  
            sum_elements += matrix[i][j]
            count_elements += 1

if operation == 'S':
    print(f"{sum_elements:.1f}")
elif operation == 'M':
    if count_elements > 0:
        average = sum_elements / count_elements
        print(f"{average:.1f}")
    else:
        print("0.0")