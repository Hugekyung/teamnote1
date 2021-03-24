n = int(input())
join_list = []
for i in range(n):
    age, name = input().split()
    join_list.append([i, int(age), name])

join_list.sort(key=lambda x: (x[1], x[0]))
for j in join_list:
    print(j[1], j[2])