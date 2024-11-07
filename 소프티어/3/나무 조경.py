import sys
import itertools

def sum_heights(indexs):
    s = 0
    for index in indexs:
        s += heights[index[0]][index[1]]
    return s

def caculate(n):
    max = 0
    if n == 2:  # 2x2 크기인 경우
        for height in heights:
            max += sum(height)
    else:  # 3x3 or 4x4 크기인 경우
        pairs = []
        all = []  # 8개인 순서쌍들

        for index in coordinates:
            for i in range(n):
                for j in range(2):
                    nx = index[i][0] + dx[j]
                    ny = index[i][1] + dy[j]
                    if 0 <= nx < n and 0 <= ny < n:
                        pairs.append([index[i], (nx, ny)])

        cb = itertools.combinations(pairs, 4)

        for c in cb:
            s1 = set(c[0] + c[1] + c[2] + c[3])
            if len(s1) == 8:
                all.append(s1)
        for i in all:
            s = sum_heights(i)
            if s > max:
                max = s
    return max

input = sys.stdin.readline

n = int(input())
heights = [list(map(int, input().split())) for _ in range(n)]

coordinates = [[(i, j) for i in range(n)] for j in range(n)]
dx, dy = (0, 1), (1, 0)  # 우, 하

max = caculate(n)

print(max)