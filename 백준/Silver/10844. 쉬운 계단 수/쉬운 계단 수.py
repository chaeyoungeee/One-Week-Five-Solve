import sys

input = sys.stdin.readline

n = int(input())
dp = [[1] * 10 for _ in range(n)]
dp[0][0] = 0

for i in range(1, n):
    for j in range(10):
        if j == 0: # 첫번째 요소
            dp[i][j] = dp[i-1][j+1]
        elif j == 9: # 마지막 요소
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[-1]) % pow(10, 9))