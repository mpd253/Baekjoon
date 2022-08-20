n, m = input().split()

n = int(n)
m = int(m)

# n-m 변수 저장
n_minus_m = n-m

# nCm 계산 결과 변수 저장, 1로 초기화
ncm = 1

# nCm 분자 부분
for num in range(2, n+1):
    ncm *= num

# nCm 분모 부분, n-m까지 반복
for num in range(2, n_minus_m + 1):
    ncm //= num

# nCm 분모부분, 2~m까지 반복    
for num in range(2, m+1):
    ncm //= num

print(ncm)