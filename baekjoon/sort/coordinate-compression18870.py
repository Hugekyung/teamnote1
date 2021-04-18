"""시간초과"""
n = int(input())
coors = list(map(int, input().split()))

for coor in coors:
    count = 0
    for co in set(coors):
        if coor > co:
            count += 1
    print(count, end=' ')


"""퀵정렬을 응용한 코드...시간초과"""
n = int(input())
coors = list(map(int, input().split()))

def quick_sort(arr, pivot):
    if len(arr) <= 1:
        return 0
    
    left = [x for x in set(arr) if x < pivot]
    return len(left)

for coor in coors:
    print(quick_sort(coors, coor), end=' ')


"""
- 중복을 제거한 리스트 상에서 각 값이 위치하는 인덱스 위치를 리턴
- 중복을 제거한 리스트에서 자신의 위치가 곧 자기보다 작은 값의 개수다
"""
n = int(input())
coors = list(map(int, input().split()))
uni_coors = list(sorted(set(coors)))
uni_coors = {val:idx for idx, val in enumerate(uni_coors)}
for i in coors:
    print(uni_coors[i], end=' ')