test = int(input())
for t in range(test):
    h, w, n = map(int, input().split())
    if h == n:
        print("{}01".format(h))
    elif h < n:
        room_num = n // h
        floor = n % h
        if floor == 0:
            floor = h
            if len(str(room_num)) < 2:
                print("{}0{}".format(floor, room_num))
            else:
                print(floor, room_num, sep='')
        else:
            room_num += 1
            if len(str(room_num)) < 2:
                print("{}0{}".format(floor, room_num))
            else:
                print(floor, room_num, sep='')
    else:
        print("{}01".format(n))