from collections import Counter

def dec_to_bin(n):
    result = ""
    if n == 0:
        return "0"
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result

def solution(s):
    result = [0, 0]
    
    while s != '1':
        c = Counter(list(s))
        result[0] += 1
        result[1] += c['0']
        s = dec_to_bin(c['1'])
        
    return result
    
    