k, n = map(int, input().split())
data = [ int(input()) for _ in range(k) ]
start, end = 1, max(data)


def solution(start, end, mid):
    while start <= end:
        mid = (start + end) // 2
        l = 0
        for d in data:
            l += d // mid
        if l >= n:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(solution(start, end, (start + end) // 2))