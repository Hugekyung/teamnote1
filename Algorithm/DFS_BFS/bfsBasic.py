"""
BFS: Breadth First Search 너비우선탐색
그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
큐 자료구조를 사용한다.

1. 탐색 시작 노드를 큐에 삽입하고 방문처리한다.
2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접노드 중 방문하지 않은 노드를 모두 큐에
   삽입하고 방문처리한다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
"""

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
        [], # 1부터 시작하기 때문에 0번째 인덱스는 비워서 처리
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)