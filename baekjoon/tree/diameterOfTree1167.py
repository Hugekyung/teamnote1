from collections import deque
import sys

# 슬라이싱으로 접근하면 경우에 따라 값이 틀리는 경우가 발생하는 듯?
# V = int(input())
# tree = [[] for _ in range(V+1)]
# for i in range(1, V+1):
#     info = list(map(int, input().split()))[1:-1]
#     for idx in range(0, len(info), 2):
#         tree[i].append((info[idx], info[idx+1]))

V = int(input())
tree = [[] for _ in range(V+1)]
for i in range(1, V+1):
    info = list(map(int, input().split()))
    for idx in range(1, len(info) - 2, 2):
        tree[info[0]].append((info[idx], info[idx+1]))

"""아무 노드에서 가장 멀리 있는 노드를 구하고,
다시 그 노드에서부터 가장 멀리 있는 노드를 구한다."""
def longest_distance(tree, start):
    visited = [-1] * (V+1) # 방문처리와 동시에 해당 노드까지의 거리 저장!!
    visited[start] = 0
    dq = deque()
    dq.append(start)
    max_dt = [0, 0] # 거리, 정점

    while dq:
        node = dq.popleft()
        for i, dt in tree[node]:
            if visited[i] == -1:
                visited[i] = visited[node] + dt
                dq.append(i)
                if max_dt[0] < visited[i]:
                    max_dt = visited[i], i

    return max_dt

distance, node = longest_distance(tree, 1)
distance, node = longest_distance(tree, node)
print(distance)