size = int(input())
num = []
for i in range(size):
    num.append(list(map(int, input().split())))
start = 2
for i in range(1, size):
    for j in range(start):
        # 맨 왼쪽이면 위에서 내려오는 친구와 더하기
        if j == 0:
            num[i][j] = num[i][j] + num[i-1][j]
        # 맨 오른쪽이면 위에서 내려오는 친구와 더하기
        elif j == i:
            num[i][j] = num[i][j] + num[i-1][j-1]
        # 가운데면 내려오는 친구들 중 최댓값과 더하기
        else:
            num[i][j] = num[i][j] + max(num[i-1][j-1], num[i-1][j])
    start += 1
print(max(num[size-1]))