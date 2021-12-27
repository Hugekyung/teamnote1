from collections import deque
import sys

def dfs(graph, start, visited):
    print(start, end=' ')
    visited[start] = True

    for node in sorted(graph[start]):
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, start, visited):
    dq = deque([start])
    visited[start] = True

    while dq:
        v = dq.popleft()
        print(v, end=' ')
        for node in sorted(graph[v]):
            if not visited[node]:
                dq.append(node)
                visited[node] = True

n, m, start = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split(' '))
    if y not in graph[x]: graph[x].append(y)
    if x not in graph[y]: graph[y].append(x)

visited = [0] * (n+1)
dfs(graph, start, visited)
print()
visited = [0] * (n+1)
bfs(graph, start, visited)