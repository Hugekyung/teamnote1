"""n개 수의 최소공배수를 리턴
파이썬에서는 math 모듈의 gcd함수를 통해 최대공약수를 쉽게 구현할 수 있다.
"""
from math import gcd

def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y) # 두 수의 곱에서 최대공약수를 나눠주면 최소공배수를 구할 수 있다.

    """# arr배열 안에서 두 수를 꺼내 두 수의 최소공배수를 구하고,
    그 결과와 다음 수와의 최소공배수를 구하는 알고리즘을 반복한다."""
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1: # 모든 계산이 끝나고 최종 값 하나만 남았을 때
            return arr[0]