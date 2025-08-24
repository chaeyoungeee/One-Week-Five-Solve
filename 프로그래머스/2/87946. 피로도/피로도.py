from itertools import permutations
from pprint import pprint

def solution(k, dungeons):
    l = len(dungeons)
    dungeons.sort(reverse=True)
    dungeons = list(permutations(dungeons, l))
    result = 0

    for dungeon in dungeons:
        left = k
        cnt = 0
        for d in dungeon:
            if left < d[0]: break
            cnt += 1
            left -= d[1]
            result = max(result, cnt)
        if result == l: break
        
    return result
                
            
    