'''
산술평균 : N개의 수들의 합을 N으로 나눈 값 / 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값 / 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''
########

########
# n = sys.stdin.readline()
# for _ in range(n):
#     num_list.append(sys.stdin.readline())

# num_list = [1, 3, 8, -2, 2]
# n = len(num_list)
import sys, heapq
from collections import Counter


num_list = []
n = int(sys.stdin.readline())
for _ in range(n):
    heapq.heappush(num_list, int(sys.stdin.readline()))

result_list = []
result_list.append(int(round(sum(num_list)/n)))
result_list.append(num_list[n//2])

num_cnt = Counter(num_list)
most_com = num_cnt.most_common()
if len(most_com) == 1:
    mode = most_com[0][0]
else:
    mode = most_com[1][0]

result_list.append(mode)
result_list.append(max(num_list)-min(num_list))

for i in result_list:
    print(i)