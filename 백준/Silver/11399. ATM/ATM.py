import sys

input = sys.stdin.readline
n = int(input())
times = list(map(int, input().split()))
times.sort(reverse=True)
time = 0

for idx, t in enumerate(times):
    time += (idx + 1) * t

print(time)