# https://www.acmicpc.net/problem/9095

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0,1,0,0]
    for i in range(1, n):
        pass


t = int(input())
ott = [1, 2, 4]
for i in range(3, 10):
    ott.append(ott[i - 3] + ott[i - 2] + ott[i - 1])
for i in range(t):
    n = int(input())
    print(ott[n - 1])