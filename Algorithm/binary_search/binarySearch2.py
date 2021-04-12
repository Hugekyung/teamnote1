# 비재귀적 이진탐색 방법

def binary_search(array, value):
    first, last = 0, len(array)
    while first <= last:
        mid = (first + last) // 2
        if array[mid] == value:
            return mid
        if array[mid] > value:
            last = mid -1
        else:
            first = mid + 1
    return False # 찾고자 하는 값이 없는 경우