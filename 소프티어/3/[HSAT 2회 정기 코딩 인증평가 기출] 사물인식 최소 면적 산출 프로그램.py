import sys

def dfs(depth, min_x, max_x, min_y, max_y):
    global min_area

    # 모든 색상이 하나씩 선택된 경우
    if depth == K:
        current_area = (max_x - min_x) * (max_y - min_y)
        min_area = min(min_area, current_area)
        return

    # 현재 면적이 최소 면적 큰 경우
    current_area = (max_x - min_x) * (max_y - min_y)
    if current_area >= min_area:
        return

    for x, y in data[depth]:
        new_min_x = min(min_x, x)
        new_max_x = max(max_x, x)
        new_min_y = min(min_y, y)
        new_max_y = max(max_y, y)
        dfs(depth + 1, new_min_x, new_max_x, new_min_y, new_max_y)

input = sys.stdin.readline
N, K = map(int, input().split())
data = [[] for _ in range(K)]

for _ in range(N):
    x, y, k = map(int, input().split())
    data[k - 1].append((x, y))

min_area = 1e9
min_x, max_x = 1001, -1001
min_y, max_y = 1001, -1001
dfs(0, min_x, max_x, min_y, max_y)

print(min_area)