"""이진탐색을 활용한 코드.. 시간초과"""
import sys

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            if target in arr[low:high+1]:
                count += arr[low:high+1].count(target)
                return count
        if target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return count

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split()))
for t in arr2:
    print((binary_search(arr, t)), end=' ')


"""Counter 함수를 사용한 코드"""
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
counter = Counter(arr)
for i in arr2:
    print(counter[i], end=' ')

