def solution(n, a, b):
    round = 0
    
    while a != b:
        a, b = (a+1)//2, (b+1)//2
        round+=1
        
    return round
                