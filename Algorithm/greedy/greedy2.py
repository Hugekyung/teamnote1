"""
각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로
하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어
결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터
순서대로 이루어진다고 가정한다.

예를 들어, 02984라는 문자열로 만들 수 있는 가장 큰 수는
((((0+2)x9)x8)x4) =576이다.
"""

string = input()

result = int(string[0])

for i in range(1, len(string)):
    num = int(string[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)