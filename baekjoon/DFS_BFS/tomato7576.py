'''보관된 토마토가 며칠이 지나면 다 익게 되는지, 그 최소 일수를 구하기
- 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
- 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
- 토마토가 모두 익지는 못하는 상황이면 -1을 출력 --> -1에 막혀 함수가 끝났는데 여전히 0인 토마토가 있다면 -1 출력
- BFS가 맞는듯, 가까운 토마토부터 순차적으로 익어가야 하니까
'''

from collections import deque

def getLeastDays(dq, tomatos, m, n):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
            #     continue
            # if tomatos[nx][ny] == (-1 or 1):
            #     continue
            # elif tomatos[nx][ny] == 0:

            if 0 <= nx < n and 0 <= ny < m and tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                dq.append((nx, ny))

m, n = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(n)]
dq = deque()
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            dq.append((i, j))

getLeastDays(dq, tomatos, m, n)
least_days = 0
for i in tomatos:
    for j in i:
        if j == 0:
            print(-1)
            exit(0) # 프로그램 정상 종료
    least_days = max(least_days, max(i))
print(least_days - 1)

# 일반 for문으로 값을 찾는 것과 flatten_list를 만들어 찾는 것 속도 비교
# if 0 in sum(tomatos, []): print(-1)
# else: print(max(sum(tomatos, []))-1)