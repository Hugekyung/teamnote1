# 해시 문제: 딕셔너리 사용
def solution(participant, completion):
    dic = {}
    for i in participant:
        dic[i] = dic.get(i, 0) + 1 # get함수는 해당 key의 value를 가져온다. get(key, default값)으로 구성되는데, 해당 값이 없으면 default값을 출력한다.
    for i in completion:
        dic[i] -= 1
    result = [key for key, value in dic.items() if value > 0] # 0보다 큰 값, 즉 1의 값을 가진 key를 찾는다.
    return result[0]