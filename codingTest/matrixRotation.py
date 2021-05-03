"""2021 Dev-Matching 웹 백엔드: 행렬 테두리 회전하기"""
def solution(rows, columns, queries):
    matrix = [[] * rows for _ in range(rows)]
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            matrix[i-1].append((i-1) * columns + j)

    result = []
    for sx, sy, ex, ey in queries:

        # 위쪽 테두리
        tmp = matrix[sx-1][sy-1] # 왼쪽 위 모서리
        tmp2 = matrix[sx-1][ey-1] # 오른쪽 위 모서리
        min_val = tmp
        for i in range(ey-1, sy-1, -1):
            matrix[sx-1][i] = matrix[sx-1][i-1]
            min_val = min(min_val, matrix[sx-1][i-1])
            
        # 오른쪽 테두리
        tmp3 = matrix[ex-1][ey-1] # 오른쪽 아래 모서리
        min_val = min(tmp2, min_val)
        for i in range(ex-1, sx, -1):
            matrix[i][ey-1] = matrix[i-1][ey-1]
            min_val = min(min_val, matrix[i-1][ey-1])
        matrix[sx][ey-1] = tmp2 # 오른쪽 위 모서리 값을 (3,4)의 위치에 넣어준다.
        
        # 아래쪽 테두리
        tmp4 = matrix[ex-1][sy-1] # 왼쪽 아래 모서리
        min_val = min(tmp3, min_val)
        for i in range(ey-1, sy):
            matrix[ex-1][i] = matrix[ex-1][i-1]
            min_val = min(min_val, matrix[ex-1][i-1])
        matrix[ex-1][ey-2] = tmp3
        
        # 왼쪽 테두리
        
        min_val = min(tmp, min_val)
        for i in range(ex-1, sx-2):
            matrix[i][sy-1] = matrix[i-1][sy-1]
            min_val = min(min_val, matrix[i-1][sy-1])
        matrix[ex-2][sy-1] = tmp4
        
        result.append(min_val)
        
    return result

rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, queries))