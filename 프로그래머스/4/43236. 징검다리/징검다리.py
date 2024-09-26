def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    start, end = 0, distance
    
    while start <= end:
        mid = (start+end)//2
        del_cnt = 0
        prev = 0
        for rock in rocks:
            dist = rock - prev
            if dist < mid:
                del_cnt += 1
                if del_cnt > n:
                    break
            else:
                prev = rock
        if del_cnt > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
                    
    return answer