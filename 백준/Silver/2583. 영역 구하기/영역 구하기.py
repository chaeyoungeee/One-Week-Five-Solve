from collections import deque
from pprint import pprint

def bfs(i, j, n, m, visited):
  que = deque([(i, j)])
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  a = 1
  visited[i][j] = 0
  while que:
    x, y = que.popleft()
    for k in range(4):
      nx, ny = x + dx[k], y + dy[k]
      if 0 <= nx < n and 0 <= ny < m:
        if visited[nx][ny] == -1:
          que.append((nx, ny))
          a += 1
          visited[nx][ny] = 0
  return a

n, m, k = map(int, input().split())
visited = [[-1] * m for _ in range(n)]
count = 0
area = []

for _ in range(k):
  ip = list(map(int, input().split()))
  for i in range(ip[1], ip[3]):
    for j in range(ip[0], ip[2]):
      visited[i][j] = -2

for i in range(n):
  for j in range(m):
    if visited[i][j] == -1:
      count += 1
      a = bfs(i, j, n, m, visited)
      area.append(a)

area.sort()
print(count)
print(" ".join(map(str, area)))
