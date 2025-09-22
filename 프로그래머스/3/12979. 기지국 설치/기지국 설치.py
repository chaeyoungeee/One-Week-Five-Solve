import math

def solution(n, stations, w):
    count = 0
    prev = 1
    
    for station in stations:
        next = station - w
        if next > prev:
            count += math.ceil((next - prev) / (w*2+1))
        prev = station + w + 1

    if prev < n:
        count += math.ceil((n - prev) / (w*2+1))
    if prev == n:
        count += 1
    
    return count