import sys

input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n - 1)]
a, b = map(int, input().split())
times.append([a, b, 0, 0])
sum_a, sum_b, a, b = 0, 0, 0, 0

for i in range(n):
    a = min(sum_a + times[i][0], sum_b + times[i][1] + times[i][3])
    b = min(sum_b + times[i][1], sum_a + times[i][0] + times[i][2])
    sum_a, sum_b = a, b

print(min(sum_a, sum_b))