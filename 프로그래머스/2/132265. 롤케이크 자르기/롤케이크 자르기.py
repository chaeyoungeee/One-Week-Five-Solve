def divide(topping):
    s = set([topping[0]])
    n = len(topping)
    dp = [0] * (n-1)
    dp[0] = 1
    
    for i in range(1, n-1):
        t = topping[i]
        dp[i] = dp[i-1]  
        
        if t not in s:
            s.add(t)
            dp[i] += 1
            
    return dp
    
    

def solution(topping):
    n = len(topping)
    result = 0
    
    dp1 = divide(topping)
    
    topping.reverse()
    dp2 = divide(topping)
    
    for i in range(n-1):
        if dp1[i] == dp2[n-2-i]:
            result += 1
            
    return result
        
