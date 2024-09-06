from collections import deque

n, k = map(int, input().split())
locations = [-1] * 100001

def bfs():
    q = deque([n])
    locations[n] = 0
    while q:
        x = q.popleft()
        nx = [x-1, x+1, x*2]
        for i in nx:
            if 0 <= i <= 100000 and locations[i] == -1:
                q.append(i)
                locations[i] = locations[x] + 1
            if i == k:
                return locations[i]

print(bfs())