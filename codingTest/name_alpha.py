""" 1번 

    이름 식별
    dog --> dogA
    cat --> catA
    dog --> dogB
    A ~ Z 까지 26개의 알파벳을 붙인다
"""

def solution(name_list):
    alpha = [chr(i) for i in range(65, 91)]
    result = []
    for name in name_list:
        for a in alpha:
            tmp_name = name + a
            if tmp_name not in result:
                result.append(tmp_name)
                break
                
    return result