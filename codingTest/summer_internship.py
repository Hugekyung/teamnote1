"""1번"""
import re

def solution(code, day, data):
    result = []
    for d in data:
        d = list(d.split(' '))
        if code in d[1] and day in d[2]:
            price = re.sub('price=', '', d[0])
            time = d[2][-2:]
            result.append((price, time))
    result = sorted(result, key=lambda x: x[1])
    answer = []
    for i,j in result:
        answer.append(int(i))
    return answer

code = '012345'
day = '20190620'
data = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]
print(solution(code, day, data))