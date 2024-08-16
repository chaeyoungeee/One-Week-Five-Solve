import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
coins.sort(reverse=True)
cnt = 0

for c in coins:
    cnt += k // c
    k %= c

print(cnt)