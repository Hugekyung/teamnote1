# 가지고 있는 랜선 개수 k, 필요한 랜선의 개수 n
import sys

k, num = map(int, sys.stdin.readline().split())

wires = []
for _ in range(k):
    wire = int(sys.stdin.readline())
    wires.append(wire)

start = 1
end = max(wires)

"""최대 랜선의 길이를 찾기 위한 이진탐색"""
result = []
while start <= end:
    count = 0
    mid = (start + end) // 2
    for wire in wires:
        count += wire // mid
    if count < num:
        end = mid - 1
    else: # count >= num인 경우
        result.append(mid)
        start = mid + 1 # 최대 개수를 찾기 위해 탐색을 계속한다.
print(max(result))