""" 코딜리티 Lesson 2: OddOccurrencesInArray"""

from collections import Counter

def solution(A):
    result = Counter(A)
    for num, cnt in result.items():
        if cnt % 2 == 1:
            return num