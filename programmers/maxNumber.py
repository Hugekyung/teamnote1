# 정렬-가장 큰 수

# 첫번째 코드, 시간초과..
from itertools import permutations

def solution(numbers):
    number_lst = []
    for i in permutations(numbers, len(numbers)):
        s = ''
        for j in i:
            s += str(j)
        if number_lst == [] or int(s) > number_lst[0]:
            number_lst.append(int(s))
    max_num = str(max(number_lst))
    return max_num

# 다른사람 풀이, 람다 함수 사용
def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key=lambda x : x*3, reverse=True) # 문자열끼리 비교해야하므로 숫자가 1000이하인 점을 이용해 같은 문자를 3번 반복한 후 비교-정렬한다.
    return str(int(''.join(num))) # 값이 '000'인 경우, int형 변환으로 0으로 만든 뒤 다시 '0' 출력.