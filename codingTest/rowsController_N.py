"""2021 카카오 인턴십 - 3번 표편집
n의 범위가 5 ≤ n ≤ 1,000,000 이고,
cmd의 범위도 1 ≤ cmd의 원소 개수 ≤ 200,000로 크기 때문에
일반적인 리스트로 구현하게 되면 효율성 테스트를 통과하지 못할 가능성이 크다..
"""


from collections import deque

def solution(n, k, cmd):
    tables = [i for i in range(n)]
    result = ["O"] * n
    tt = tables.copy()
    del_list = deque()
    
    for c in cmd:
        if c[0] == "D" or c[0] == "U":
            tmp = list(c.split())
            if tmp[0] == "U":
                k -= int(tmp[1])
            if tmp[0] == "D":
                k += int(tmp[1])
        elif c[0] == "C":
            del_list.append(tt.pop(k))
            try:
                tmp = tt[k]
            except:
                k -= 1
        elif c[0] == "Z":
            tmp = del_list.pop()
            tt.insert(tmp, tmp)
            if tmp <= k:
                k += 1
        print("현재 위치는: ", k)

    for i in del_list:
        result[i] = "X"
    result = ''.join(result)
    return result

cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(8, 2, cmd))

