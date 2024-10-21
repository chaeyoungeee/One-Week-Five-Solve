n = int(input())
celebrities = [ tuple(map(int, input().split())) for _ in range(n) ]
x = 0

for c in celebrities:
    pi, ci = c
    if abs(pi - x) <= ci:
        x += 1

print(x)