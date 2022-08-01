a, b = map(int, input().split())

matrixA = []
matrixB = []

for i in [matrixA, matrixB]:
    for j in range(a):
        i.append(list(map(int, input().split())))

for i in range(a):
    for j in range(b):
        matrixA[i][j] += matrixB[i][j]
    print(*matrixA[i])