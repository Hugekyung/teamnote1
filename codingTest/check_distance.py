""" 2021 카카오 채용연계형 인턴십 - 거리두기 확인하기 """
from collections import deque

def bfs(x, y, place):
    dx = [0, 0, -1, 1] # 좌, 우
    dy = [-1, 1, 0, 0] # 상, 하

    visited = [[0]*5 for _ in range(5)]
    
    dq = deque()
    dq.append((x, y))
    visited[x][y] = 1
    
    
    while dq:
        px, py = dq.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            
            if x == nx and y == ny:
                continue
            if nx < 0 or ny < 0 or nx > 4 or ny > 4:
                continue
            if visited[nx][ny] == 1:
                continue
            if place[nx][ny] == 'X':
                continue
            if place[nx][ny] == 'P':
                # print('P 좌표:', (nx, ny))
                man_dis = abs(x-nx) + abs(y-ny)
                # print("맨해튼거리:", man_dis)
                if man_dis <= 2:
                    return 0
            if place[nx][ny] == 'O':
                dq.append((nx, ny))
                visited[nx][ny] = 1
                # print("다음좌표:", (nx, ny))
    return 1

        
# def solution(places):
#     result = []
#     for place in places:
#         tmp = []
#         for i, p1 in enumerate(place):
#             for j, p2 in enumerate(p1):
#                 if p2 == 'P':
#                     answer = bfs(i, j, place)
#                     tmp.append(answer)
#         if 0 in tmp:
#             result.append(0)
#         else:
#             result.append(1)
    
#     return result


# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
#             ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
#             ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], # 세 번째 대기실 틀림
#             ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
#             ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

# print(solution(places))

place = ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"] # 거리두기 잘 지킴

def sol():
    for i, p1 in enumerate(place):
        for j, p2 in enumerate(p1):
            if p2 == 'P':
                return bfs(i, j, place)

print(sol())