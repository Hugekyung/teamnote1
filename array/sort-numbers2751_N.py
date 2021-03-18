import sys

n = int(input())
numbers =[]
for _ in range(n):
    i = int(sys.stdin.readline())
    numbers.append(i)
else:
    numbers = sorted(numbers)
    [print(i) for i in numbers]