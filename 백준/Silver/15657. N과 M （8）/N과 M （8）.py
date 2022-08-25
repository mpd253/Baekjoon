import itertools

n, m = map(int, input().split())

numlist = list(map(int, input().split()))

numlist = sorted(numlist)

# 중복 조합을 사용
comb = itertools.combinations_with_replacement(numlist, m)

for i in comb:
    for j in range(m):
        print(i[j], end=' ')
    print()