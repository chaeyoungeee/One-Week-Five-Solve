def solution(N, stages):
    answer = []
    n = 0
    l = len(stages)
    fails = [[0, 1] for _ in range(N+1)]
    stages.sort(reverse=True)
    
    while stages:
        s = stages.pop()
        if s > N:
            break
        if n != s:
            n = s
            fails[n][1] = l
        fails[n][0] += 1
        l -= 1
    
    rates = []
    for i in range(1, len(fails)):
        rates.append((i, fails[i][0]/fails[i][1]))
    
    rates = sorted(rates, key=lambda x: (-x[1], x[0]))
    
    for r in rates:
        answer.append(r[0])
    return answer