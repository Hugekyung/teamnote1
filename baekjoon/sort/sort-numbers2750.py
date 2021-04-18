n = int(input())
numbers =[]
for _ in range(1, n+1):
    i = int(input())
    numbers.append(i)
numbers = sorted(numbers)
for j in numbers:
    print(j, end='\n')