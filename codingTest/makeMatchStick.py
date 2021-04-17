# 성냥개비 k 개로 만들 수 있는 숫자의 개수 return

def solution(k):
    matchStick = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6] # 2~7
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    if k <= 3: # 모두 사용해서 한가지 수밖에 만들지 못하는 수들
        if k == 1:
            return 0
        elif k == 2:
            return 1
        else: # k가 3인 경우 만들 수 있는 수는 7뿐이다.
            return 1
    else:
        pass
