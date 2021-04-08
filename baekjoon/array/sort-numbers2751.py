def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [i for i in tail if i <= pivot]
    right_side = [i for i in tail if i > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

print(quick_sort(array))