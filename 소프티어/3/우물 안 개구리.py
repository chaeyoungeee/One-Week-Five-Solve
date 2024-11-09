import sys

def update(a, b):
    if weights[b] >= max_weights[a]:
        max_weights[a] = weights[b] + 1


input = sys.stdin.readline

n, m = map(int, input().split())
weights = list(map(int, input().split()))
max_weights = weights[:]
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    update(a - 1, b - 1)
    update(b - 1, a - 1)

for i in range(n):
    if weights[i] >= max_weights[i]:
        cnt += 1

print(cnt)