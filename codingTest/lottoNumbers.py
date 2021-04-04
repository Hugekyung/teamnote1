def solution(lottos, win_nums):
    cor_count = 0
    zero_count = 0
    
    for i in lottos:
        if i == 0:
            zero_count += 1
        for j in win_nums:
            if i == j:
                cor_count += 1
    
    if zero_count == 0 and cor_count == 6:
        return [1,1]
    else:
        if cor_count == 5:
            min_rank = 2
        elif cor_count == 4:
            min_rank = 3
        elif cor_count == 3:
            min_rank = 4
        elif cor_count == 2:
            min_rank = 5
        else:
            min_rank = 6
        max_rank = min_rank-zero_count
        if max_rank == 0:
            max_rank = 1
        return [max_rank, min_rank]