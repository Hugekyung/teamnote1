n = int(input())
info = []

for _ in range(n):
    x, y = map(int, input().split())
    info.append((x, y))

print(info)
rank = []

for i in info:
    count = n # 나보다 덩치 큰 사람 수
    for j in info:
        if i == j:
            continue
        elif i[0] > j[0] and i[0] > j[0]:
            count -= 1
    rank.append(count)

print(rank)
print(' '.join(rank))