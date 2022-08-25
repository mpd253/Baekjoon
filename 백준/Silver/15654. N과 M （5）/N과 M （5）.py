import itertools

n, m = map(int, input().split())
numlist = list(map(int, input().split()))

numlist = sorted(numlist)

# 순열 사용
comb = itertools.permutations(numlist, m)

for i in comb:
    for j in range(m):
        print(i[j], end=' ')
    print()