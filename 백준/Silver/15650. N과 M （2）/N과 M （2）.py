import itertools

n, m = map(int,input().split())

li = []
for i in range(1, n+1):
    li.append(i)

nPm = itertools.combinations(li, m)

for i in nPm:
    for j in range(m):
        print(i[j], end=' ')
    print()