V = int(input())
tree = [[] for _ in range(V+1)]
for i in range(1, V+1):
    info = list(map(int, input().split()))[1:-1]
    for idx, v in enumerate(info):
        if idx % 2 == 0:
            tree[i].append((v, info[idx+1]))

visited = [False] * (V+1)

def longest_distance(tree, visited):
    visited[1] = True
    distance = tree[1][1]

    for i in tree[1:]:
        for d in i:
        if visited[i[0]]