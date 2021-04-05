def solution(n):
    count_tail = 0
    s = 1
    while n >= 5**s:
        count_tail += n // 5**s
        s += 1
    return count_tail