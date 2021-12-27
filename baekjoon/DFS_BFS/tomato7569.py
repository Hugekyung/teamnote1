'''3D 토마토'''

from collections import deque

def getLeastDays():

    while dq:
        k, x, y = dq.popleft()

        for i in range(6):
            nh, nx, ny = k + dh[i], x + dx[i], y + dy[i]

            if (0 <= nh < h) and (0 <= nx < n) and (0 <= ny < m) and (tomatos[nh][nx][ny] == 0):
                tomatos[nh][nx][ny] = tomatos[k][x][y] + 1
                dq.append((nh, nx, ny))
        
        # ### 매트릭스 확인 ###
        # for idx,i in enumerate(tomatos):
        #     print("floor >>", idx)
        #     for t in i:
        #         print(t)
        # ################################

m, n, h = map(int, input().split())
tomatos = []
for _ in range(h):
    tomatos.append([list(map(int, input().split())) for _ in range(n)])

### for test set ###
# m, n, h = 5, 3, 2
# tomatos = [
#             [[0, 0, 0, 0, 0], # 1층
#             [0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0]],
#             [[0, 0, 0, 0, 0], # 2 층
#             [0, 0, 1, 0, 0],
#             [0, 0, 0, 0, 0]]
#             ]

dq = deque()
for f in range(h):
    for i in range(n):
        for j in range(m):
            if tomatos[f][i][j] == 1:
                dq.append((f, i, j))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

getLeastDays()
least_days = 0
for h in tomatos:
    for i in h:
        for j in i:
            if j == 0:
                print(-1)
                exit(0) # 프로그램 정상 종료
        least_days = max(least_days, max(i))
print(least_days - 1)