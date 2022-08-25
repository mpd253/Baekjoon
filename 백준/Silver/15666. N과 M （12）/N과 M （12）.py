import itertools

n, m = map(int, input().split())
numlist = list(map(int, input().split()))
numlist = sorted(numlist)

# 중복 조합 사용
perm = itertools.combinations_with_replacement(numlist, m)
perm = set(perm)
perm = sorted(perm)

for i in perm:
    for j in range(m):
        print(i[j], end=' ')
    print()