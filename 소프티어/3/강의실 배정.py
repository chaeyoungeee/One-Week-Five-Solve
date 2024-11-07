import sys
import heapq

input = sys.stdin.readline
time = []
last, cnt = 0, 0
n = int(input())

for i in range(n):
    s, f = map(int, input().split())
    heapq.heappush(time, (f, -s))

while time:
    f, s = heapq.heappop(time)
    if -s >= last:
        last = f
        cnt += 1

print(cnt)