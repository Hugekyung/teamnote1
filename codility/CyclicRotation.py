"""코딜리티 Lesson 2: cyclicRotation
list가 아예 비어있는 경우의 수도 고려해야 통과"""

def solution(A, K):
    try:
        for _ in range(K):
            tmp = A.pop()
            A.insert(0, tmp)
    except:
        pass

    return A