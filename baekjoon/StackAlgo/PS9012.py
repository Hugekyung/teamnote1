import sys

n = int(sys.stdin.readline())
for _ in range(n):
    ps = sys.stdin.readline()
    ps_count = 0
    for p in ps:
        if ps_count < 0: # count가 음수로 나오는 경우 정상적인 ()의 형태가 나오지 않는 것으로 판단한다.
            answer = "NO"
            break
        elif p == '(':
            ps_count += 1
        elif p == ')':
            ps_count -= 1
    if ps_count == 0:
        print("YES")
    elif ps_count < 0:
        print(answer)
    else:
        print("NO")