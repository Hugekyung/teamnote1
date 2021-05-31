"""월간코드챌린지 - 모두 0으로 만들기"""
"""코드 뜯어보기,,, 이해 부족"""
import sys
sys.setrecursionlimit(300000)

def dfs(node, a, tree):
    global result
    global visited
    
    now = a[node]
    visited[node] = 1
    
    for i in tree[node]: # node0 -> 1, 3
        if visited[i] == 0:
            now += dfs(i, a, tree)
    
    result += abs(now)
    return now
    
def solution(a, edges):
    global result
    global visited
    result = 0
    
    if sum(a) != 0:
        return -1
    
    tree = [[] for _ in range(len(a))]
    visited = [0] * len(a)
    
    for i, j in edges:
        tree[i].append(j)
        tree[j].append(i)
        
    dfs(0, a, tree)
    return result