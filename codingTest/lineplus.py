""" liner """
"""1"""
def solution(student, k):
    if student.count(1) < k:
        return 0
    
    count = 0
    has_list = []
    
    for i in range(0, len(student)+1):
        for j in range(len(student)+1, 0, -1):
            if student[i:j] not in has_list and student[i:j].count(1) == k:
                has_list.append(student[i:j])
                count += 1
                
    return count