def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left, right = 0, distance
    
    while left <= right:
        mid = (left+right)//2
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
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
                    
    return answer