"""
알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤
그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
"""

string = input()
result = []
number = 0

for s in string:
    if s.isalpha(): # 알파벳인지 여부
        result.append(s)
    else:
        number += int(s)

result.sort() # 오름차순 정렬

if number != 0:
    result.append(str(number))

# 리스트 형태의 원소들을 붙여서 한번에 출력할 때!! join함수
print(''.join(result))