n = int(input())
A = list(map(int, input().split()))
s = sorted(A)
P = []

for a in A:
    idx = s.index(a)
    P.append(idx)
    s[idx] = -1

for p in P:
    print(p, end=" ")