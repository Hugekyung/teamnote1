"""출구로 가기 위해 지나야 하는 최소 칸 수를 구해야 하기 때문에
최적의 경로를 구하는 것과 같다. 따라서 bfs 알고리즘을 사용하자.
"""

from collections import deque

n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input())))

# 이동 방향 정의(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    dq = deque()
    dq.append((x, y))

    while dq: # 큐가 빌 때까지 반복한다.
        x, y = dq.popleft() # 현재 좌표
        for i in range(4): # 현재 위치에서 상,하,좌,우 방향으로 움직일 때
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m:
                continue
            if miro[next_x][next_y] == 0:
                continue
            if miro[next_x][next_y] == 1:
                miro[next_x][next_y] = miro[x][y] + 1
                dq.append((next_x, next_y)) # 현재위치를 추가해주고 다시 반복
    print(miro[n-1][m-1])

bfs(0, 0)