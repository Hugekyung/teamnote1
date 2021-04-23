def solution(n):
    cur = 0
    _next = 1
    for _ in range(n):
        cur, _next = _next, cur + _next 
    return cur % 1234567