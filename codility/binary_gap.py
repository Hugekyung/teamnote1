def solution(N):
    binary = bin(N)[2:]
    
    if '1' in binary and binary[-1] != '1': # 1이 있는데 마지막 값이 1이 아닌 경우
        for i in range(len(binary)-1, -1, -1):
            if binary[i] == '1':
                binary = binary[:i+1]
                break # 브레이크를 안걸면 for문이 계속 돌아서 1밖에 안남는다.
    if '0' not in binary or '1' not in binary: # 0이 없거나 1이 없는 경우
        return 0

    
    zero_list = []
    for i,b in enumerate(binary):
        if b == '1':
            j = i + 1
            while j <= len(binary)-1:
                if binary[j] == '1': # 1011, 10011
                    zero_list.append(binary[i:j+1])
                    break
                j += 1 # 1을 마지막에 더해줘야 인덱스 범위를 벗어나지 않는다.

    result = []
    for zero in zero_list:
        cnt = zero.count('0')
        result.append(cnt)
    return max(result)

solution(19)