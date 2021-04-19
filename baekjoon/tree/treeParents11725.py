from collections import deque
import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    tree[x].append(y)
    tree[y].append(x)

visited = [False] * (n+1)

def bfs(tree, root, visited):
    deq = deque([root])
    visited[root] = True
    result = {}

    while deq:
        parent = deq.popleft()
        for i in tree[parent]:
            if not visited[i]:
                deq.append(i)
                result[i] = parent
                visited[i] = True
    
    return result

parents_dic = bfs(tree, 1, visited)
for i in range(2, n+1):
    print(parents_dic[i])