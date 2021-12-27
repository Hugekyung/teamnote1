# 가장 짧은 -> bfs(최단거리)
from collections import deque

def diff_cnt(w1, w2):
    diff_cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff_cnt += 1
    return diff_cnt

def solution(begin, target, words):
    if target not in words:
        return 0
    
    dq = deque()
    dq.append((begin, 0))
    visited = [0] * len(words)
    
    while dq:
        now_word, depth = dq.popleft()
        if now_word == target:
            break
        
        for i, w in enumerate(words):
            if visited[i]:
                continue
            diff_count = diff_cnt(now_word, w)
            if diff_count == 1: # 한글자 차이인 경우 dq에 추가하고 방문처리
                depth += 1
                dq.append((w, depth))
                visited[i] = True

    return depth

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))