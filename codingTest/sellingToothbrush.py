"""2021 Dev-Matching 웹 백엔드: 다단계 칫솔 판매..시간초과
트리의 최하단에서 부모로 올라가면서 하나씩 계산을 하는데
여러 자식이 있는 부모의 경우, 자식 수 만큼 중복으로 지나가게 되어
시간초과가 발생한다."""
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

"""딕셔너리를 활용한 재귀방법-- 통과!!
위의 방식이랑 비슷하게 가는 것 같은데 시간초과가 안걸린다..
딕셔너리라서 그런가?"""
def aggregation(seller, price, tree):

    if tree[seller][0] == ' ': # 부모가 없는 경우
        return
    else:
        commission = price // 10 # 몫만, 나머지는 절사
        if commission < 1:
            tree[seller][1] += price
        else:
            rest = price - commission
            parents = tree[seller][0]
            tree[seller][1] += rest
            aggregation(parents, commission, tree)

def solution(enroll, referral, seller, amount):
    
    tree = {'-' : [' ', 0]} # 부모, 금액

    for e, r in zip(enroll, referral):
        parent = r
        tree[e] = [parent, 0]
    
    for s, a in zip(seller, amount):
        price = a * 100
        aggregation(s, price, tree)

    result = []
    for key, value in tree.items():
        result.append(value[1])
    result.pop(0)

    return result
    
"""다른 사람 코드"""
def solution(enroll, referral, seller, amount):

    tree = {'-' : 'root'} # 부모 관계 저장, 트리 구현
    sell = {'-' : 0} # 판매금액 집계
    for i in range(len(enroll)):
        child = enroll[i]
        parent = referral[i]
        sell[child] = 0 
        tree[child] = parent

    for i in range(len(seller)):
        child = seller[i]
        parent = tree[child]
        profit = amount[i] * 100
        sell[child] += profit
        while True:
            commission = profit // 10
            sell[child] -= commission
            sell[parent] += commission
            child = parent
            parent = tree[child]
            profit = commission
            if parent == 'root':
                break

    result = []
    for e in enroll:
        result.append(sell[e])

    return result


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))