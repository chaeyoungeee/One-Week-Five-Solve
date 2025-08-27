def solution(brown, yellow):
    s = brown + yellow
    answer = [0, 0]
    
    i = 3
    while s:
        if s % i == 0:
            if 2*((s//i)+i-2) == brown: 
                answer = [s // i, i]
                break
        i += 1
    
    return answer