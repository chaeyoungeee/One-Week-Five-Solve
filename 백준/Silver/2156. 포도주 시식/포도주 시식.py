import sys

input = sys.stdin.readline

n = int(input())
data = [ int(input()) for _ in range(n)]

dp = [0] * n

dp[0] = data[0]
if n > 1: dp[1] = data[1] + data[0]
if n > 2: dp[2] = max(data[2] + data[1], data[2] + data[0], dp[1])

for i in range(3, n):
    # case
    # 1. 현재(i), 1개 전(i-1) 마시기 / 2개 전(i-2) 안 마시기
    # 2. 현재(i), 2개 전(i-2) 마시기 / 1개 전(i-1) 안 마시기
    # 3. 현재(i) 안 마시기
    dp[i] = max(data[i] + data[i-1] + dp[i-3], # case 1
                data[i] + dp[i-2], # case 2
                dp[i-1] # case 3
            )

print(dp[n-1])