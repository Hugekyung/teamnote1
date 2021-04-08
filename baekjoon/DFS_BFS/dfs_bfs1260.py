from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)] # 그래프 형태 생성

# 각 노드에 연결된 값을 모아둔 그래프 리스트 생성
for _ in range(m):
    x, y = map(int, input().split())
    if y not in graph[x]:
        graph[x].append(y)
    if x not in graph[y]:
        graph[y].append(x)


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in sorted(graph[v]): # 작은 수부터 꺼내기 위한 정렬
        if not visited[i]: # 해당 노드가 False로 방문하지 않았다면
            dfs(graph, i, visited) # 그 노드를 시작노드로 해서 방문

def bfs(graph, v, visited):
    dq = deque([v])
    visited[v] = True # 현재 노드 방문처리
    
    while dq:
        node = dq.popleft() # 가장 먼저 들어온 값 추출
        print(node, end=' ')
        for i in sorted(graph[node]): # 작은 수부터 꺼내기 위한 정렬
            if not visited[i]:
                dq.append(i)
                visited[i] = True

visited = [False] * (n+1) # 인덱스 0을 제외하기 위해 n+1을 한다.
visited_bfs = visited.copy()
dfs(graph, v, visited)
print()
bfs(graph, v, visited_bfs)