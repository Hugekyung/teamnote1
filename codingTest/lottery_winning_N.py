""" 네이버웹툰 개발챌린지 1번 .. 미완성"""

def solution(lottery):
    user_dic = {}
    cnt = {}
    for lot in lottery:
        user = lot[0]
        vic_loto = lot[1]
        user_dic[user] = 0
        cnt[user] = 0
    
    for lot in lottery:
        user = lot[0]
        vic_loto = lot[1]
        cnt[user] += 1
        user_dic[user] += vic_loto
    
    total_cnt = 0
    zero_list = []
    for _id1, c in cnt.items():
        for _id2, u in user_dic.items():
            if _id1 == _id2 and u > 1:
                c = (c - u) + 1
            elif _id1 == _id2 and u == 0:
                zero_list.append(_id1)
        total_cnt += c
    if zero_list != []:
        for z in zero_list:
            del cnt[z]
    if cnt == {}:
        return 0
    result = total_cnt // len(cnt)
    return result