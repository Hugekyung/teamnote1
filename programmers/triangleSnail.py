"""
프로그래머스 [월간 코드 챌린지 시즌1]
"삼각 달팽이"
"""
def solution(n):
    # 아래, 오른쪽, 좌상향
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    numbers = n*(n+1) // 2
    layer = [[0]*i for i in range(1, n+1)]
    x, y, d, num = 0, 0, 0, 1

    while num <= numbers:
        layer[x][y] = num # 첫번째 값인 1은 어떤 경우에도 (0,0)의 위치에 들어간다.
        num += 1
        nx = x + dx[d]
        ny = y + dy[d]

        # nx, ny 값이 범위를 벗어나지 않고 layer[nx][ny]가 0으로 값이 비어있을 때
        if 0 <= nx < n and 0 <= ny < n and layer[nx][ny] == 0:
            x = nx
            y = ny
        # layer 값이 0이 아닌 수로 채워져 있거나 nx, ny값이 범위를 벗어난 경우
        else:
            d = (d+1) % 3
            x += dx[d]
            y += dy[d]
    
    return sum(layer, [])