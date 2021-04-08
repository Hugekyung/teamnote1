x = int(input())

if x == 1:
    print("1/1")
else:
    i = 2
    sum_i = 3
    while True:
        if x <= sum_i:
            if i % 2 == 0:
                start_num = sum_i - i + 1
                x_idx = x - start_num
                print("{}/{}".format(x_idx+1, i-x_idx))
                break
            else:
                start_num = sum_i - i + 1
                x_idx = x - start_num
                print("{}/{}".format(i-x_idx, 1+x_idx))
                break
        else:
            i += 1
            sum_i += i