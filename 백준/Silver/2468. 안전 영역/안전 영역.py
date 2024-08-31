from pprint import pprint
import sys
import copy
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [ list(map(int, input().split())) for _ in range(n) ]

max_h = 0
for g in graph:
    max_h = max(max_h, max(g))

cnt = 0 # 안전 영역의 수
max_cnt = 0 # 안전 영역 수의 최댓값

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j, k):
    queue = deque([(i, j)])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] >= k and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

for k in range(1, max_h+1):
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= k and visited[i][j] == 0:
                bfs(i, j, k)
                cnt += 1
    if max_cnt < cnt: max_cnt = cnt
    cnt = 0

print(max_cnt)