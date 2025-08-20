from collections import deque
from pprint import pprint

def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n, m = len(maps), len(maps[0])
    visited = [[-1] * m for _ in range(n) ]
    
    que = deque([(0, 0)])
    visited[0][0] = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
    
    return visited[n-1][m-1]
 