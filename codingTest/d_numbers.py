"""월간 코드챌린지 2-1번문제"""
def solution(left, right):
    result = 0
    for num in range(left, right+1):
        d_num = []
        for i in range(1, num+1):
            if num % i == 0:
                d_num.append(i)
        if len(d_num) % 2 == 0:
            result += num
        else:
            result -= num
    
    return result