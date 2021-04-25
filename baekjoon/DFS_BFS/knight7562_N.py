"""나이트가 최소 몇 번만에 이동할 수 있는지 출력한다 --> 최단거리 --> bfs"""
from collections import deque

# 나이트 이동방향(우하향2, 좌하향2, 우상향2, 좌상향2)(x좌표, y좌표)
move = [(2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)]

def bfs(leng, test):
    x, y = test[0]
    tx, ty = test[1]
    deq = deque()
    deq.append((x, y))

    count_list = []
    count = 1
    while deq:
        x, y = deq.popleft()
        for i in range(8):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny < 0 or nx >= leng or ny >= leng:
                continue
            if nx == tx and ny == ty:
                return count
            else:
                deq.append((nx, ny))
                count += 1


n = int(input())
for _ in range(n):
    leng = int(input())
    test = []
    for _ in range(2):
        test.append(map(int, input().split()))
    print(bfs(leng, test))