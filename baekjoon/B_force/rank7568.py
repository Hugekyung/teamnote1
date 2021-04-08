n = int(input())
info = []

for _ in range(n):
    x, y = map(int, input().split())
    info.append((x, y))

counts = []

for i in info:
    count = 1 # 나보다 덩치 큰 사람 수
    for j in info:
        if i == j:
            continue
        elif i[0] < j[0] and i[1] < j[1]:
            count += 1

    counts.append(str(count))

print(' '.join(counts))