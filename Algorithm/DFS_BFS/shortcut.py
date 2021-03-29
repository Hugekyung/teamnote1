"""
N x M 크기의 직사각형 형태의 미로가 있다. 현재 위치는 (1,1)이며 미로의 출구는
(n,m)의 위치에 존재하며 한 번에 한 칸씩, 인접한 칸으로만 이동할 수 있다.
이때, 1은 이동할 수 있는 칸이며 0은 이동할 수 없는 칸을 나타낸다.
현재 위치에서 미로를 탈출하기 위한 위치까지 움직여야 하는 최소 칸의 개수를
구하라.(단, 시작 칸과 마지막 칸을 모두 포함한다.)
"""

from collections import deque

# n, m 입력받기
n, m = map(int, input().split())

# 미로 정보 입력받기
miro = []
for _ in range(n):
    miro.append(list(map(int, input())))

# 이동 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0] # 그래프상 올라가려면 -1을 해야 위로, 내려가려면 +1
dy = [0, 0, -1, 1]

# (x, y)는 시작 위치의 좌표
def bfs(x, y):
    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # map의 범위를 벗어났을 때
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽이 있을 때
            if miro[nx][ny] == 0:
                continue
            # 지나갈 수 있는 길일 때
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1 # 칸의 횟수를 세기 위해 +1
                dq.append((nx, ny)) # 현재 위치를 deque에 추가
    return miro[n-1][m-1] # (n, m)으로 이동하기 위해 지나간 칸의 횟수

print(bfs(0, 0))