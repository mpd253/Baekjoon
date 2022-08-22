# 반복 횟수
test = int(input())

for i in range(test):
    # 층
    floor = int(input())
    # 호
    room = int(input())
    # 0층 사는 친구들
    bottom = [l for l in range(1, room+1)]
    for j in range(floor):
        li = []
        # 호수를 다 더해서 li에 추가
        for k in range(room):
            li.append(sum(bottom[:k+1]))
        # 리스트 반환하면서 반복
        bottom = li.copy()
    print(li[k])