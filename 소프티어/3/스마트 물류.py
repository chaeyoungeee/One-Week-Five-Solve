import sys

input = sys.stdin.readline
n, k = map(int, input().split())
data = list(input())
cnt = 0

for i in range(n):
    if data[i] == 'P':
        for j in range(-k, k+1):
            t = i+j
            if t < 0 or t >= n:
                continue
            if data[t] == 'H':
                data[t] = -1
                cnt += 1
                break

print(cnt)