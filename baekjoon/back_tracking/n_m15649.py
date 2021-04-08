# 순열을 이용한 문제풀이
import itertools

n, m = map(int, input().split())

n_lst = [str(i) for i in range(1, n+1)]
result = itertools.permutations(n_lst, m)
for r in result:
    tmp = list(r)
    print(' '.join(tmp))