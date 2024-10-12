N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
S  = 0

for z in zip(A, B):
    S += z[0] * z[1]

print(S)