A, B, C = map(int, input().split())

if C <= B or C < 1:
    print(-1)
else:
    n = A / (C - B)
    print(int(n)+1)