# 퀵정렬 첫번째 방법보다 간단한 코드
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    #첫번째 원소인 5보다 작은 값들을 왼쪽 리스트로
    left_side = [x for x in tail if x <= pivot]
    #첫번째 원소인 5보다 큰 값들을 오른쪽 리스트로
    right_side = [x for x in tail if x > pivot]

    # quick_sort를 재귀적으로 반복 실행해서 정렬을 수행한다.
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))