while True:
    N = int(input())
    if N == 0:
        break

    matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            value = min(i, j, N - 1 - i, N - 1 - j) + 1
            matrix[i][j] = value

    for i in range(N):
        for j in range(N):
            if j == 0:
                print(f"{matrix[i][j]:>3}", end="")
            else:
                print(f" {matrix[i][j]:>3}", end="")
        print()
    print() 