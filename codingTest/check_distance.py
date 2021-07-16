""" 2021 카카오 채용연계형 인턴십 - 거리두기 확인하기 """
""" 맨해튼 거리는 결국 이동한 좌표의 거리 수 이므로 이동한 거리만큼 숫자를 카운트하고,
또 다른 정점인 P를 만났을 때까지의 거리가 2 이내일 경우 0, 2 초과이면 1을 반환하면 된다."""

from collections import deque

def bfs(x, y, place):
    dx = [0, 0, -1, 1] # 좌, 우
    dy = [-1, 1, 0, 0] # 상, 하

    visited = [[0]*5 for _ in range(5)]
    
    dq = deque()
    dq.append((x, y))
    px, py = x, y # 처음 시작한 P 좌표를 저장
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if px == nx and py == ny: # 처음 시작한 P 좌표와 이동한 좌표가 겹치지 않게!(제일 중요)
                continue
            if nx < 0 or ny < 0 or nx > 4 or ny > 4:
                continue
            if visited[nx][ny] != 0: # 이미 방문한 경우
                continue
            if place[nx][ny] == 'X': # 칸막이인 경우
                continue
            if place[nx][ny] == 'P': # 처음 출발한 P로부터 가장 가까운 P를 만났을 때
                visited[nx][ny] += visited[x][y] + 1
                if visited[nx][ny] <= 2:
                    return 0
            if place[nx][ny] == 'O':
                dq.append((nx, ny))
                visited[nx][ny] += visited[x][y] + 1 # visited에 이동한 거리를 합산기록한다.

    return 1

        
def solution(places):
    result = []
    for idx, place in enumerate(places):
        tmp = []
        for i, p1 in enumerate(place):
            for j, p2 in enumerate(p1):
                if p2 == 'P':
                    answer = bfs(i, j, place)
                    tmp.append(answer)
        if 0 in tmp:
            result.append(0)
        else:
            result.append(1)
    
    return result


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))