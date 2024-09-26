n, c = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort()
start, end = 1, data[len(data) - 1]

def solution(start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        prev, cnt = data[0], 1
        for i in range(1, len(data)):
            dist = data[i] - prev
            if dist >= mid:
                cnt += 1
                prev = data[i]
                if cnt > c:
                    break
        if cnt >= c:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer

print(solution(start, end))