def solution(n, info):
    result = [0] * 11
    answer = [-1]
    m = 0
    
    def backtrack(k, left, ascore, rscore):
        nonlocal m, answer
        if k == -1 or left == 0:
            ascore2 = ascore
            
            if k != -1:
                for i in range(k, -1, -1):
                    if info[i]:
                        ascore2 += (10-i)
            else:
                result[10] += left

            if ascore2 < rscore and m < (rscore - ascore2):
                m = rscore - ascore2
                answer = result[:]
            result[10] = 0
            return
        
        for j in [info[k]+1, 0]: 
            if j > left:
                ascore += 10-k
                backtrack(k-1, left, ascore, rscore)
            else:        
                rscore2, ascore2 = rscore, ascore
                if j > info[k]:
                    rscore2 += 10-k
                elif j < info[k]:
                    ascore2 += 10-k
                result[k] = j 
                backtrack(k-1, left-j, ascore2, rscore2)
            result[k] = 0

    backtrack(10, n, 0, 0)
    return answer