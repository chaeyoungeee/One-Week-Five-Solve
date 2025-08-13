def next(k):
    return (k + 1) // 2 if k % 2 else k // 2 

def solution(n, a, b):
    round = 1
    
    while True:
        if (a % 2 and (a + 1) == b) or (not (a % 2) and (a - 1) == b):
                return round
        round += 1
        a, b = next(a), next(b)
        
                
                