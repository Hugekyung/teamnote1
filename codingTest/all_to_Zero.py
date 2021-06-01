"""월간코드챌린지 - 모두 0으로 만들기"""
"""코드 뜯어보기,,, 이해 부족,,, 생각보다 쉬운문제다"""
import sys
sys.setrecursionlimit(300000)

def dfs(node, a, tree):
    global result
    global visited
    print("현재 가중치는 {}입니다.".format(a[node]))
    
    now = a[node] # 가중치
    visited[node] = 1
    
    for i in tree[node]:
        if visited[i] == 0:
            print("현재 노드는 {}입니다.".format(node))
            now += dfs(i, a, tree)
    
    result += abs(now) # 누적 실행횟수를 구해야하므로 절댓값으로 더한다.
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

a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))