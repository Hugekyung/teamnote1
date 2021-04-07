# k번째 최소값
import heapq

def kth_smallest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    print(heap)
    
    kth_min = None
    for _ in range(k):
        kth_min = heapq.heappop(heap) # 앞에서부터 k번 최소값 제거 후 값 갱신
    return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))