""" 코딜리티 Lesson 3: Time Comlexity """

def solution(X, Y, D):
    total_dis = Y - X
    
    count = total_dis // D
    rest = total_dis % D
    if rest > 0:
        count += 1

    return count