import sys

input = sys.stdin.readline

k, p, n = map(int, input().split())
n *= 10

result = (k * pow(p, n, 1000000007)) % 1000000007

print(result)