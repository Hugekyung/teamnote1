n = int(input())

max_des = 2
i = 1
while True:
    if n >= max_des:
        max_des = max_des + (6 * i)
        i += 1
    else:
        i -= 1
        pre = max_des - (6 * i)
        now = max_des
        numbers = now - pre
        room_count = numbers / 6
        print(int(room_count+1))
        break