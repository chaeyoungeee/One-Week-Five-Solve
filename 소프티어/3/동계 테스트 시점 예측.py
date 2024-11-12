import sys
from collections import deque

def bfs():
    visited = [[0] * m for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny]:
                    visited[nx][ny] += 1
                elif not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                graph[i][j] = 0

input =  sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in  range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

while True:
    s = 0
    for i in range(n):
        s += sum(graph[i])
    if s == 0:
        break
    bfs()
    cnt += 1

print(cnt)