def solution(s):
    result = []
    s = list(s[2:-2].split("},{"))
    s.sort(key=lambda x: len(x))
    
    for i in s:
        k = set(map(int, i.split(','))) - set(result)
        result.extend(list(k))
    
    return result
    