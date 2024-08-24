import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [0] * n
dp[0] = data[0]

for i in range(1, n):
    a, b = dp[i - 1] + data[i], data[i]
    if  a > b: dp[i] = a
    else: dp[i] = b

print(max(dp))