"""
프로그래머스 [월간 코드 챌린지 시즌1]
"두개 뽑아서 더하기"
"""
def solution(numbers):
    result = []
    for i, v in enumerate(numbers):
        for j in numbers[i+1:]:
            num = v + j
            if num not in result:
                result.append(num)
    result.sort()
    return result

"""itertools의 combinations를 사용한 코드"""
from itertools import combinations 

def solution(numbers):
    return list(sorted(set([sum(combs) for combs in combinations(numbers, 2)])))