import sys
com_num = int(sys.stdin.readline())
n = int(sys.stdin.readline())

visited = [False] * (com_num+1) # 0번째 인덱스는 안쓰니까 +1을 해준다.
graphs = [[] for _ in range(com_num+1)]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if b not in graphs[a]:
        graphs[a].append(b)
    if a not in graphs[b]:
        graphs[b].append(a)

def virus(graphs, v, visited): # dfs 방식 사용
    visited[v] = True

    for g in graphs[v]:
        if not visited[g]:
            virus(graphs, g, visited)
    
    return visited.count(True)-1 # 1번 컴퓨터 자기자신은 count에서 제외

print(virus(graphs, 1, visited))