# 최대 힙
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num))  # (우선 순위, 값)
    print(heap)
while heap:
    # heappop은 가장 작은 값을 출력하므로 -num이 작을 수록 실제 값은 가장 크다.
    print(heapq.heappop(heap)[1])  # index 1(값 출력)