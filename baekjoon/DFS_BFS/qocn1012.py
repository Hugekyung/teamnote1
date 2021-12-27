from collections import deque

def get_worms_cnt(graph, sx, sy, n, m):
    global worm_cnt
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    dq = deque()
    dq.append((sx, sy))
    if graph[sx][sy] == 1: graph[sx][sy] = 0
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1: 
                graph[nx][ny] = 0; 
                dq.append((nx, ny))
        
    worm_cnt += 1

test_case = int(input())
for _ in range(test_case):
    worm_cnt = 0 
    n, m, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                get_worms_cnt(graph, i, j, n, m)
    print(worm_cnt)