n = int(input())
coors = []
for _ in range(n):
    coor = list(map(int, input().split()))
    coors.append((coor[0], coor[1]))

coors.sort(key=lambda x: (x[1], x[0]))
for coor in coors:
    print(coor[0], coor[1])