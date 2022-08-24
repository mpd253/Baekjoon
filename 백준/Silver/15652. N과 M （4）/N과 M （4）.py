import itertools

n, m = map(int,input().split())

li = []
for i in range(1, n+1):
    li.append(i)

# 중복 조합 메서드인 ..._with_replacement 사용
nPm = itertools.combinations_with_replacement(li, m)

for i in nPm:
    for j in range(m):
        print(i[j], end=' ')
    print()