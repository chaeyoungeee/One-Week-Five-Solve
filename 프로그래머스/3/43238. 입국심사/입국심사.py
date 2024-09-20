def solution(n, times):
    an = n // len(times) # 심사관 당 평균 할당 사람 수
    start, end = min(times) * an, max(times) * an
    
    while start <= end:
        middle = (start + end) // 2
        mp = 0
        for t in times:
            mp += middle // t
        if mp < n:
            start = middle + 1
        else:
            end = middle - 1
            
    return start