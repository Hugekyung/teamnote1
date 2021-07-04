""" 네이버웹툰 개발챌린지 2번 .. 미완성 """

from collections import deque

def path_sum(miro):
    dx = [1, 0] # 오른쪽
    dy = [0, 1] # 아래
    
    all_cnt = 0
    for i in miro:
        all_cnt += len(i)
    n = all_cnt
    m = len(miro)
    
    dq = deque()
    dq.append((1, 1))

    while dq:
        x, y = dq.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # map의 범위를 벗어났을 때
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            miro[nx][ny] += miro[x][y]
            dq.append((nx, ny)) # 현재 위치를 deque에 추가
    return miro[n-1][m-1]

def solution(grid):
    miro = grid
    sum_list = []
    sum_list.append(path_sum(miro))
    result = min(sum_list)
    return result

grid = [ [1, 2], [3, 4] ]
solution(grid)