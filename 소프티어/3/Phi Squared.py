import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
data = deque([i + 1, size] for i, size in enumerate(a))

while len(data) > 1:
    q = deque()
    while data:
        now = data.popleft()
        left, right = 0, 0
        if q:
            left = q.pop()
        if data:
            right = data.popleft()

        new = now[:]
        if left:
            if now[1] >= left[1]:
                new[1] += left[1]
            else:
                q.append(left)
        if right:
            if now[1] >= right[1]:
                new[1] += right[1]
            else:
                data.appendleft(right)
        q.append(new)
    data = deque(list(q)[:])

print(data[0][1])
print(data[0][0])