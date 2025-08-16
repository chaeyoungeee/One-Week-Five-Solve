from sys import stdin
from collections import deque

input = stdin.readline
m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    que = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                que.append((i, j))

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    que.append((nx, ny))

bfs()

result = 0
for r in maps:
    if 0 in set(r):
      result = -1
      break
    result = max(result, max(r)-1)

print(result)