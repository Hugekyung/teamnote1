""" N** 코테 """

""" 1번 문제 - 테케 3개 시간초과"""

def solution(s):
    if 'a' not in s or 'z' not in s:
        return 0
    
    result = 0
    for i,v in enumerate(s):
        if v == 'z':
            for j,k in enumerate(s[i+1:]):
                if k == 'a' and 'z' not in s[i+1:j+i+1] and 'a' not in s[i+1:j+i+1]:
                    result += 1
        elif v == 'a':
            for j,k in enumerate(s[i+1:]):
                if k == 'z' and 'z' not in s[i+1:j+i+1] and 'a' not in s[i+1:j+i+1]:
                    result += 1
                    
    return result


""" 2번 - 해결못함"""
from collections import deque

def makenumber(b):
    alpha = b[0]
    x_num = int(b[1])
    if alpha == 'A':
        return (1, x_num)
    elif alpha == 'B':
        return (2, x_num)
    elif alpha == 'C':
        return (3, x_num)
    elif alpha == 'D':
        return (4, x_num)
    elif alpha == 'E':
        return (5, x_num)
    elif alpha == 'F':
        return (6, x_num)
    elif alpha == 'G':
        return (7, x_num)
    elif alpha == 'H':
        return (8, x_num)

def bfs(now, chess):
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]
    
    dq = deque()
    dq.append(now)
    x, y = now
    px, py = x, y
    
    count = 0
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print("현재좌표 :", (nx, ny))

            if nx < 1 or ny < 1 or nx > 8 or ny > 8:
                continue
            if chess[nx][ny] != 0: # 이미 방문한 경우
                continue
            if chess[nx][ny] == 0:
                dq.append((nx, ny))
                chess[nx][ny] == 1
                count += 1
                
    return count
    
def solution(bishops):
    if len(bishops) == 64:
        return 0
    
    chess = [[0] * 9 for _ in range(9)]
    
    count = 0
    for b in bishops:
        now = makenumber(b)
        count += bfs(now, chess)
        
    return 64 - count


bishops = ["C6"]
print(solution(bishops))