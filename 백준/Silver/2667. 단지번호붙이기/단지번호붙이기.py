import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [ list(map(int, input().strip())) for _ in range(n) ]

cnt = 0 # 해당 단지의 집 수
houses = [] # 단지별 집 수 저장 리스트

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    global cnt
    cnt += 1
    graph[i][j] = 0
    queue = deque([(i, j)])

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)
            houses.append(cnt)
            cnt = 0

houses.sort()
print(len(houses))
for house in houses:
    print(house)