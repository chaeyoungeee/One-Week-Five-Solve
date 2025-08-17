def solution(n, words):
    round = 1
    p = 1
    w = {words[0]}
    
    for i in range(1, len(words)):
        p = (i % n) + 1 # 번호
        round = (i // n) + 1 # 차례
        
        if words[i-1][-1] != words[i][0] or words[i] in w:
            return [p, round]
        
        w.add(words[i])
        
    return [0, 0]
    
    
        
        
        
        