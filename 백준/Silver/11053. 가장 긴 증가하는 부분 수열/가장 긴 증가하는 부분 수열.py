n = int(input())
a = list(map(int, input().split()))

# 0으로 다 채우는 배열 생성
num = [0] * n

for i in range(n):
    for j in range(i):
        # 첫번째 인덱스부터 수열의 길이 최댓값 저장
        if a[i] > a[j] and num[i] < num[j]:
            num[i] = num[j]
    num[i] += 1
print(max(num))