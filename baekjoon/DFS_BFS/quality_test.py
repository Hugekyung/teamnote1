import time

matrix = [[9, 8, 7, 6, 5, 4],
        [8, 7, 6, 5, 4, 3],
        [7, 6, 5, 4, 3, 2],
        [6, 5, 4, 3, 2, 1]]

# for문
st = time.time()
for i in matrix:
    for j in i:
        if j == 1:
            print("spend time >>", time.time() - st)

# sum을 활용한 flatten list
st = time.time()
flatten = sum(matrix, [])
if 1 in flatten: print("spend time >>", time.time() - st)

print("=========")
# 결론 한줄의 코드로 짜기에는 sum이 효율적이지만, 속도면에서는 for문이 좋다.