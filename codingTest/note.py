# """카카오인턴 - 3번문제"""

# def solution(n, k, cmd):
#     result = ['O'] * n
#     test = [i for i in range(n)]
#     remove_list = []
#     cur = k
#     for c in cmd:
#         c = list(c.split(' '))
#         if c[0] == 'D':
#             cur += int(c[1])
#         elif c[0] == 'U':
#             cur -= int(c[1])
#         elif c[0] == 'C':
#             if (len(test) - 1) == cur:
#                 remove_list.append(test.pop(cur))
#                 cur -= 1
#             else:
#                 remove_list.append(test.pop(cur))
#         elif c[0] == 'Z':
#             if remove_list[-1] <= cur:
#                 cur += 1
#             test.insert(remove_list[-1], remove_list[-1])
#             remove_list.pop(-1)
#     for r in remove_list:
#         result[r] = 'X'
#     return ''.join(result)

# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
# solution(8, 2, cmd)

"""카카오인턴 5번문제"""
num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
print(sum(num), sum(num)//3)