def solution(S, C):
    s_list = S.split(',')
    C = C.lower()

    email_list = []
    name_list = []
    for s in s_list:
        s = s.lower()
        tmp_list = list(s.split())

        if "-" in tmp_list[-1]:
            tmp_list[-1] = tmp_list[-1].replace("-", '')

        front_email = tmp_list[0] + "." + tmp_list[-1]
        name_list.append(front_email)

    for i,n in enumerate(name_list):
        _email = f" <{n}@{C}.com>"
        s_list[i] += _email

    result = ','.join(s_list)
    return result

S = "John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker"
C = "Example"
print(solution(S, C))