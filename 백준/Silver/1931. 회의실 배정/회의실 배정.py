import sys

input = sys.stdin.readline
n = int(input())
times = [ list(map(int, input().split())) for _ in range(n) ]
times.sort(key=lambda x: (x[1], x[0]))
end, cnt = 0, 0

for t in times:
    if end <= t[0]:
        cnt += 1
        end = t[1]

print(cnt)