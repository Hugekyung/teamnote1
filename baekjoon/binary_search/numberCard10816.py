import sys

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            if target in arr[low:mid]:
                count += arr[low:mid+1].count(target)
            elif target in arr[mid:high]:
                count += arr[mid:high].count(target)
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