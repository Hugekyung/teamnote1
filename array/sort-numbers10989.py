import sys
n = int(sys.stdin.readline())

counting = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    counting[num] += 1

for i, c in enumerate(counting[1:]):
    if c != 0:
        for _ in range(c):
            print(i+1)