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
    new_graph[i][j] = 0
    queue = deque([(i, j)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if new_graph[nx][ny] >= k:
                new_graph[nx][ny] = 0
                queue.append((nx, ny))

for k in range(1, max_h+1):
    new_graph = copy.deepcopy(graph) # 깊은 복사
    for i in range(n):
        for j in range(n):
            if new_graph[i][j] >= k:
                bfs(i, j, k)
                cnt += 1
    if max_cnt < cnt: max_cnt = cnt
    cnt = 0

print(max_cnt)