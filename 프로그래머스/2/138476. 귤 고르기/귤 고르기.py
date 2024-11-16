from collections import Counter

def solution(k, tangerine):
    cnt = 0
    tangerine = sorted(Counter(tangerine).items(), key=lambda x: -x[1])
    for t in tangerine:
        k -= t[1]
        cnt += 1
        if k <= 0:
            return cnt
    
    