# heapq 알고리즘을 활용한 힙정렬

import heapq

array = [5,7,9,0,3,1,6,2,4,8]

def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    print(heap)

    sorted_nums = []
    while heap:
        # heappop을 통해 가장 작은 값을 순서대로 리스트에 넣는다.
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums

print(heap_sort(array))