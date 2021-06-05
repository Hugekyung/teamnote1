def solution(string):
    ten_num = 0
    
    for i, s in enumerate(string):
        try:
            if string[i+1] <= s:
                # ten_num += 1
                print(s)
                if string[i+1:i+3] > s: # 두 자리 수
                    # print(string[i+1:i+3])
                    ten_num += 1
                elif string[i+1:i+4] > s: # 세 자리 수
                    ten_num += 10
        except:
            break
    
    result = int(str(ten_num) + string[-1])
    return result
string = '2349101'
print(solution(string))
print(string[2:5])
