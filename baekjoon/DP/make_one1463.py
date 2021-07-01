import sys

n = int(sys.stdin.readline())

# 최소 값 경로를 저장하기 위한 리스트
# 인덱스 0번째는 단순히 인덱스 순서를 맞춰주기 위한 값이고
# 인덱스 1부터 n == 1인 경우, n == 2, n == 3일 때의 출력값이다.
dp = [0,0,1,1]

# (예시) N = 10 → 9 → 3 → 1 = 출력 : 3
for i in range(4, n+1): # 4 ~ 10
    print("현재 i값: ", i)
    dp.append(dp[i-1]+1) # -1을 수행할 때의 횟수 count?
    print("현재 dp: ", dp)
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i]) # n을 2로 나누었을 때 나머지의 연산 횟수와 현재 횟수 중 최소 count 저장
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    print("연산 후 dp 상태:", dp)

print(dp[n])