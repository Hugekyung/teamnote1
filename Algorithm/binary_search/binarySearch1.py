# 재귀함수로 구현하는 이진탐색
# 이진탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법

def binary_search(array, value, low, high):
    if low > high:
        return False
    mid = (low + high) / 2
    if array[mid] > value: # 중간값이 찾고자 하는 값보다 클 때
        return binary_search(array, value, low, mid-1) # low ~ mid-1 범위에서 value를 찾는다.
    elif array[mid] < value:
        return binary_search(array, value, mid+1, high) # mid+1 ~ high 범위에서 찾는다.
    else: # array[mid] == value인 경우
        return mid