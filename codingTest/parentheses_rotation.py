"""월간 코드 챌린지 시즌2 -- 괄호 회전하기(level 2)"""

from collections import deque

def solution(s):
    result = 0
    
    if len(s) % 2 == 1:
        return result
    
    opens = ['[', '(', '{']
    ends = [']', ')', '}']
    dq = deque(s)
    for _ in range(len(s)):
        dq.append(dq.popleft())
        if dq[0] == ']' or dq[0] == ')' or dq[0] == '}':
            continue
            
        stack = []
        for v in dq:
            if v in opens:
                stack.append(v)
            elif v in ends and stack != []:
                for i in range(3):
                    if stack[-1] == opens[i] and v == ends[i]:
                        stack.pop()
                        break """<--여기 break 왜걸지???"""
                
        if not stack:
            result += 1
            
    return result

s1 = "}]()[{"
print(solution(s1))