n = int(input())
dp = [i for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        if j**2 > i:
            break
        k =  dp[i - j**2] + 1
        if dp[i] > k: dp[i] = k

print(dp[n])