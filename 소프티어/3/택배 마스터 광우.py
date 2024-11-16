import sys
import itertools

input = sys.stdin.readline
N, M, K = map(int, input().split())
weights = list(map(int, input().split()))
result = 1e9

permutation = list(itertools.permutations(weights))

while permutation:
    pr = permutation.pop()
    i, k, m = 0, K, M
    cnt = 0 # 일한 횟수
    s = 0 # 무게합
    while True:
        m -= pr[i]
        if m < 0:
            cnt += 1
            if cnt == K:
                break
            m = M
            continue
        s += pr[i]
        i += 1
        if i >= N:
            i = 0
    result = min(result, s)

print(result)
