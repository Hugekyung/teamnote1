"""나이트가 최소 몇 번만에 이동할 수 있는지 출력한다 --> 최단거리 --> bfs"""
from collections import deque
import sys

# 나이트 이동방향(우하향2, 좌하향2, 우상향2, 좌상향2)(x좌표, y좌표)
move = [(2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)]

def bfs(leng, test):
    x, y = test[0]
    tx, ty = test[1]
    deq = deque()
    deq.append((x, y))

    while deq:
        x, y = deq.popleft()

        if x == tx and y == ty:
            print(chess[tx][ty])
            break

        for i in range(8):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny < 0 or nx >= leng or ny >= leng:
                continue
            elif chess[nx][ny] == 0:
                deq.append((nx, ny))
                chess[nx][ny] = chess[x][y] + 1


n = int(sys.stdin.readline())
for _ in range(n):
    leng = int(sys.stdin.readline())
    test = []
    chess = [[0] * leng for _ in range(leng)]
    for _ in range(2):
        test.append(map(int, sys.stdin.readline().split()))
    bfs(leng, test)