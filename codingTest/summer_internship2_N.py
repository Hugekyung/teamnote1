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