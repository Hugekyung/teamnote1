"""단지번호붙이기 문제
bfs방식 사용
1. 1을 만날 때마다 cnt값을 1씩 증가(집 개수)
2. 지나간 위치 값을 0으로 변환(지나간 곳을 중복방문하지 않기 위해)

틀림_다시 풀어보기
"""
from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 단지 수 세기
def bfs(x, y, visited):
    deq = deque()
    deq.append((x, y))
    visited[x][y] == 1
    cnt = 0

    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                print(nx, ny)
                deq.append((nx, ny))
                visited[nx][ny] == 1
                cnt += 1
            
    return cnt

n = int(input())
graph = []
for _ in range(n):
    arr = list(map(int, input()))
    graph.append(arr)
visited = [[0] * n for _ in range(n)]

cnt_list = []

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
cnt = bfs(0, 0, visited) # 무한반복되는 문제가 뭔가 있는디,,
cnt_list.append(cnt)

cnt_list.sort()
print(len(cnt_list))
for i in cnt_list:
    print(i)


"""dfs방식_정답"""
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# cnt = 0
# apt = []

# def dfs(x, y):
#     global cnt
#     graph[x][y] = 0
#     cnt += 1

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or ny < 0 or nx >= n or ny >= n:
#             continue
#         if graph[nx][ny] == 1: # 주변에 연결된 1이 없어질 때까지 반복
#             dfs(nx, ny)

# n = int(input())
# graph = []
# for _ in range(n):
#     arr = list(map(int, input()))
#     graph.append(arr)

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             cnt = 0
#             dfs(i, j) # 인접한 단지 하나에 1이 모두 0으로 될 때까지
#             apt.append(cnt) # 해당 단지에 있던 1의 개수를 apt에 담는다.

# apt.sort()
# print(len(apt)) # apt의 개수 자체가 단지의 개수이다.
# for i in apt:
#     print(i)