n = int(input())
coors = []
for _ in range(n):
    coor = list(map(int, input().split()))
    coors.append((coor[0], coor[1]))

coors.sort(key=lambda x: (x[0], x[1]))
for coor in coors:
    print(coor[0], coor[1])