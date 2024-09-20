n, m = map(int, input().split())
data = list(map(int, input().split()))
end = max(data) # 최대: 가장 긴 나무
start = end - m # 최소: 가장 긴 나무 - 가져가려는 나무 길이

def solution(start, end, mid):
    while start <= end:
        mid = (start + end) // 2
        h = 0
        for d in data:
            if d > mid:
                h += d - mid
        if h >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(solution(start, end, (start + end) // 2))