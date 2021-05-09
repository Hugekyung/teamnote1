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

"""2번_ 해결못함"""
def solution(t, r):
    info = []
    result = []
    for i in range(len(t)):
        info.append((t[i], r[i], i)) # (도착시각, 티켓등급, 아이디 값)
    info = sorted(info, key=lambda x: (x[0], x[1], x[2]))
    for i in range(len(info)):
        for j in range(i, len(info)):
            if i == j:
                continue
            if info[i][0] >= info[j][0]:
                if info[i][1] <= info[j][1]:
                    result.append(info[i][2])
                else:
                    result.append(info[j][2])
            else:
                result.append(info[i][2])
    return result


t = [0,1,3,0]
r = [0,1,2,3]
print(solution(t, r))