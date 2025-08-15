import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(x, cnt):
    global result
    cnt += 1
    if cnt == 5: 
        result = 1
        return
    for i in r[x]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, cnt)
            visited[i] = 0

n, m = map(int, input().split())
r = [[] for _ in range(n)]
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    r[a].append(b)
    r[b].append(a)

for i in range(n):
    visited = [0] * n
    visited[i] = 1
    dfs(i, 0)
    if result == 1:
        break

print(result)