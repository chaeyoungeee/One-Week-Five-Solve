import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [ list(map(int, input().strip())) for _ in range(n) ]
visited = [ [-1] * m for _ in range(n) ]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 1
    while True:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
            if nx == n-1 and ny == m-1:
                return visited[nx][ny]


print(bfs())

