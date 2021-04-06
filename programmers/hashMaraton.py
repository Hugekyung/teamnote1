# 해시 문제: 딕셔너리 사용
def solution(participant, completion):
    dic = {}
    for i in participant:
        dic[i] = dic.get(i, 0) + 1
    for i in completion:
        dic[i] -= 1
    result = [key for key, value in dic.items() if value > 0]
    return result[0]