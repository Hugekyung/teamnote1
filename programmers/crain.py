def solution(board, moves):
    remove_cnt = 0
    stack = [0]
    n = len(board)
    before = stack[-1]
    for move in moves:
        x = 0
        move -= 1
        while True:
            if not board[n-1][move]: # 해당 열에 인형이 하나도 없을 때
                break
            if not board[x][move]:
                x += 1
                continue
            else:
                item = board[x][move]
                board[x][move] = 0
                if item == before:
                    stack.pop(-1)
                    remove_cnt += 2
                else:
                    stack.append(item)
                before = stack[-1]
                break
        
    return remove_cnt

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))