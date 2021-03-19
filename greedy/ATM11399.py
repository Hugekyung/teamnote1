people = int(input())
time = list(map(int, input().split()))

time.sort()
min_time = 0
for i in range(people):
    min_time += sum(time[:i+1])

print(min_time)