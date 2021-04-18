import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    elif x == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap)[1])