# 최대 힙
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num))  # (우선 순위, 실제 값)
    print(heap)
while heap:
    # heappop은 가장 작은 값을 출력하므로 -num이 작을 수록 실제 값은 가장 크다.
    print(heapq.heappop(heap)[1])  # index 1(값 출력)

# 두번째 방법
for num in nums:
    heapq.heappush(heap, -num)
for i in range(len(nums)):
    print(-heapq.heappop(heap)) # -를 출력값 앞에 붙여서 -를 제거한다.