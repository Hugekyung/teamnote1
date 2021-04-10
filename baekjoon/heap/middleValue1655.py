import sys
import heapq

n = int(sys.stdin.readline())
left_heap = [] # 최대 힙
right_heap = [] # 최소 힙
for _ in range(n):
    x = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-x, x))
    else:
        heapq.heappush(right_heap, x)

    # left_heap의 top이 홀수일 경우는 중간값이 되고, 짝수인 경우에는 
    # right_heap의 top과 대수비교를 해서 위치를 변경해야 한다.
    # left_heap의 top이 right_heap의 top보다 크면 두 수의 위치를 바꾼다.
    if right_heap and left_heap[0][1] > right_heap[0]:
        tmp_left = heapq.heappop(left_heap)[1]
        tmp_right = heapq.heappop(right_heap)
        heapq.heappush(left_heap, (-tmp_right, tmp_right))
        heapq.heappush(right_heap, tmp_left)
    print(left_heap[0][1]) 