def solution(n, words):
    answer = [] 
    ws = set()  
    ws.add(words[0])  
    
    for k in range(1, len(words)):
        i = (k % n) + 1 
        j = (k // n) + 1  
        
        if words[k] in ws:
            return [i, j] 
        
        if words[k][0] != words[k-1][-1]:
            return [i, j] 
        
        ws.add(words[k])
    
    return [0, 0]