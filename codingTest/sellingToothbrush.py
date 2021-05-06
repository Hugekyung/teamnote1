"""2021 Dev-Matching 웹 백엔드: 다단계 칫솔 판매"""
def aggregation(idx, rest, referral, enroll, result):
    first_head = referral[idx] # 7, edward
    if first_head == "-":
        return result
    else:
        idx = enroll.index(first_head) # 2
        if int(rest * 0.1) < 1:
            result[idx] += rest
            return result
        pre_rest = rest
        rest = int(rest * 0.1) # 120 * 0.1, 1원 미만 절사
        profit = pre_rest - rest
        result[idx] += profit # edward가 108원 플러스
        aggregation(idx, rest, referral, enroll, result)

def solution(enroll, referral, seller, amount):
    result = [0] * len(enroll) # enroll 순서대로 집계 금액
    
    seller_amount = [(seller[i], amount[i] * 100) for i in range(len(seller))]

    for present in seller_amount:
        _seller, _amount = present # young, 1200 / tod, 200
        rest = int(_amount * 0.1) # 120 / 20
        profit = _amount - rest # 1080 / 180
        
        idx = enroll.index(_seller) # 7
        result[idx] += profit # young 자리에 1080원 플러스
        aggregation(idx, rest, referral, enroll, result)

    return result