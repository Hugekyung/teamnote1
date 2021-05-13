"""월간코드챌린지2 -2번문제...시간초과 2개"""
def solution(numbers):
    result = []
    for num in numbers:
        origin_num = num
        while True:
            bit_num = bin(origin_num)[2:]
            num += 1
            bit_next = bin(num)[2:]
            diff = 0
            if len(bit_num) < len(bit_next):
                bit_num = '0' + bit_num
            for i in range(len(bit_num)):
                if diff > 2:
                    break
                if bit_num[i] != bit_next[i]:
                    diff += 1
            if 0< diff <= 2:
                result.append(num)
                break
            
    return result

numbers = [2, 7]
print(solution(numbers))