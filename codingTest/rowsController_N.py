"""2021 카카오 인턴십 - 3번 표편집
n의 범위가 5 ≤ n ≤ 1,000,000 이고,
cmd의 범위도 1 ≤ cmd의 원소 개수 ≤ 200,000로 크기 때문에
일반적인 리스트로 구현하게 되면 효율성 테스트를 통과하지 못할 가능성이 크다..
"""

""" 내코드 - 테케도 절반이상, 효율성은 전부 통과못함 """
# from collections import deque

# def solution(n, k, cmd):
#     tables = [i for i in range(n)]
#     result = ["O"] * n
#     tt = tables.copy()
#     del_list = deque()
    
#     for c in cmd:
#         if c[0] == "D" or c[0] == "U":
#             tmp = list(c.split())
#             if tmp[0] == "U":
#                 k -= int(tmp[1])
#             if tmp[0] == "D":
#                 k += int(tmp[1])
#         elif c[0] == "C":
#             del_list.append(tt.pop(k))
#             try:
#                 tmp = tt[k]
#             except:
#                 k -= 1
#         elif c[0] == "Z":
#             tmp = del_list.pop()
#             tt.insert(tmp, tmp)
#             if tmp <= k:
#                 k += 1
#         print("현재 위치는: ", k)

#     for i in del_list:
#         result[i] = "X"
#     result = ''.join(result)
#     return result

# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
# print(solution(8, 2, cmd))


""" 다른 사람 풀이 - 테케&효율성 절반정도 통과 못함.. """
import heapq

def solution(n, k, cmd):
    # 현재 위치: right의 첫 번째 원소.
    
    left, right, rm = [], [], []
    
    for i in range(n):
        heapq.heappush(right, i)
    for i in range(k):
        heapq.heappush(left, -heapq.heappop(right))
        
    for c in cmd:
        command = c[0]
        if command == "D":
            move = int(c[-1])
            for _ in range(move):
                if right:
                    heapq.heappush(left, -heapq.heappop(right))
        
        elif command == "U":
            move = int(c[-1])
            for _ in range(move):
                if left:
                    heapq.heappush(right, -heapq.heappop(left))
                    
        elif command == "C":
            rm.append(heapq.heappop(right))
            if not right:
                heapq.heappush(right, -heapq.heappop(left))
        elif command == "Z":
            restore = rm.pop()
            
            if restore < right[0]:
                heapq.heappush(left, -restore)
            else:
                heapq.heappush(right, restore)
    
    result = []
    while left:
        result.append(-heapq.heappop(left))
    while right:
        result.append(heapq.heappop(right))
    result = set(result) # 정렬
    answer = ["O" if i in result else "X" for i in range(n)]
    
    return ''.join(answer)