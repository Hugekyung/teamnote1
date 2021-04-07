# 기본적인 힙은 최소힙을 기준으로 한다.

import heapq

heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

# 힙 원소 삭제
print(heapq.heappop(heap)) # 가장 작은 값 삭제
print(heap)

# 기존 리스트를 힙으로 변환
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)