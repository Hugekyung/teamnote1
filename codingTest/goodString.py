def solution(s):
    result = 1
    if len(s) == 1:
        return result
    else:
        if len(set(s)) == 1:
            return result
        else:
            tmp = []
            for i in range(len(s)):
                for j in range(len(s)):
                    if len(s[i:j+1]) != len(set(s[i:j+1])):
                        continue
                    else:
                        tmp.append(s[i:j+1])
            result = len(list(set(tmp))[1:])
            return result