from collections import deque

def solution(numbers, target):
    result = 0
    dq = deque()
    dq.append((numbers[0], 0)); dq.append((-numbers[0], 0))
    plus_minus = [1, -1]

    while dq:
        num, idx = dq.popleft()
        idx += 1

        if idx < len(numbers):
            for i in range(2):
                # num += numbers[idx] * plus_minus[i] 
                # ==> 이 방법이 안되는 이유 : for문을 돌면서 num변수가 갱신되기 때문에 기존의 num이 없어지게 된다. 즉, 잘못된 변수를 사용하게 된다.
                next_num = numbers[idx] * plus_minus[i] # 독립적인 변수에 담아줘야 한다.
                dq.append((num+next_num, idx))
        else:
            if num == target:
                result += 1

    return result

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))