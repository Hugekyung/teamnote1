n, m = map(int, input().split())
card_num = list(map(int, input().split()))

result = []
for num in card_num:
    for nu in card_num:
        for n in card_num:
            if num != nu and num != n and nu != n and (num + nu + n) == m:
                card_sum = num + nu + n
                result.append(card_sum)
                break
            elif num != nu and num != n and nu != n and (num + nu + n) < m:
                card_sum = num + nu + n
                result.append(card_sum)
print(max(result))