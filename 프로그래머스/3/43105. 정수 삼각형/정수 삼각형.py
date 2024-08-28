def solution(triangle):
    dp = triangle[0]
    
    for i in range(1, len(triangle)):
        dp = [triangle[i][j] 
              + max(dp[j-1] if j > 0 else 0, dp[j] if j < i else 0) 
              for j in range(i+1)]
    
    return max(dp)