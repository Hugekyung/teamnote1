import sys
import heapq

n = int(input())
heap = []
for i in range(1, n+1):
    x = int(input())
    heapq.heappush(heap, x)
    if i % 2 == 1: # 홀수이면
        print(heap[round(i / 2) - 1])
    else: # 짝수인 경우
        print(heap[(i // 2) - 1])