"""일반적인 for문을 활용하면 투입 데이터의 크기에 따라 시간복잡도가
증가하므로 시간초과가 발생한다."""
n = int(input())
arr = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))
for x in arr2:
    if x in arr:
        print(1)
    else:
        print(0)

"""위와 같은 코드이지만, 자료구조를 set으로 바꾸게 되면 시간초과가
발생하지 않는다. list 자료구조에서 search는 O(n) 시간복잡도를 가지지만,
set 자료구조를 사용하면 중복값이 제거되기도 하고 값 접근에도 O(1) 시간복잡도를
가지게 되어 시간초과 없이 문제를 해결할 수 있다!!!"""
n = int(input())
arr = set(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))
for x in arr2:
    if x in arr:
        print(1)
    else:
        print(0)

"""이진탐색 방법"""
"""해결안됨..런타임 에러?(typeError)"""
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return 1
        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return 0

n = int(input())
arr = list(map(int, input().split())).sort()
m = int(input())
arr2 = list(map(int, input().split()))
for t in arr2:
    print(binary_search(arr, t))


"""아래 코드는 되는데..?"""
import sys

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return 1
        if target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return 0

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))
for t in arr2:
    print(binary_search(arr, t))