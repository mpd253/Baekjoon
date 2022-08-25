import itertools

n, m = map(int, input().split())
numlist = list(map(int, input().split()))
numlist = sorted(numlist)

# 순열 사용
perm = itertools.permutations(numlist, m)
perm = set(perm)
perm = sorted(perm)

for i in perm:
    for j in range(m):
        print(i[j], end=' ')
    print()