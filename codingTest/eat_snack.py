"""2번
    세션 시작까지 남은 시간 동안 쉬지 않고 먹을 수 있는 간식의 개수를 출력하는 함수를 작성해주세요.

    단, 간식의 개수는 가능한 한 적어야 합니다.
"""
def solution(seconds):
    snack_dic = {'300': 10, '130': 30, '120': 20, '20': 30}
    snack_list = [300, 130, 120, 20]
    
    count = 0

    while seconds > 0:
        if seconds == 0:
            break
        for time in snack_list:
            if time <= seconds and snack_dic[str(time)] > 0:
                tmp = seconds - time
                if tmp < 120 and tmp % 20 != 0:
                    continue
                else:
                    seconds -= time
                    snack_dic[str(time)] -= 1
                    count += 1
                    break
               
    return count


print(solution(460)) # incorrect