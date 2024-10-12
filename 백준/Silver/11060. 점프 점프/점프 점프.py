n = int(input())
data = list(map(int, input().split()))
dp = [n] * n
dp[0] = 0

for i in range(len(data)):
    for j in range(data[i]):
        k = i + j + 1
        if k < n:
            dp[k] = min(dp[k], dp[i] + 1)

if dp[n-1] == n:
    print(-1)
else:
    print(dp[n-1])
