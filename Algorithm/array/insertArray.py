array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 0까지 1씩 감소하는 반복문
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동하며 크기 비교
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자신보다 작은 값을 만나면 멈춤
            break

print(array)