"""단지번호붙이기 문제
bfs 방법을 사용해 1을 만날 때마다 count를 해주는 방식으로?
"""
from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    deq = deque()
    deq.append((x, y))

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                deq.append((nx, ny))

    return graph[nx-1][ny-1]

n = int(input())
graph = []
for _ in range(n):
    arr = list(map(int, input()))
    graph.append(arr)

print(bfs(0, 0))