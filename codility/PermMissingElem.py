""" 코딜리티 Lesson 3: Time Complexity - PermMissingElem 
1 ~ N까지의 숫자가 담긴 리스트에서 빠진 숫자 1개가 무엇인지 찾아 리턴.
for문을 사용하면 시간초과가 발생.
1 ~ N까지 숫자 합인 total_sum을 구한 뒤, 임의의 숫자 1개가 빠진 리스트A의
합인 arr_sum을 빼주면 빠진 값이 무엇인지 빠르게 찾을 수 있다.
"""

def solution(A):
    N = len(A) + 1
    total_sum = N * (N+1) // 2
    arr_sum = sum(A)

    result = total_sum - arr_sum
    return result