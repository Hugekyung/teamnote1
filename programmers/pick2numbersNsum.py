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