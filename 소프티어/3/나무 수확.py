import sys

input = sys.stdin.readline
n = int(input())
crops = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0] * n for _ in range(n)]  # (방문한 열매 중 최댓값, 방문한 열매 합)
dx, dy = (0, 1), (1, 0)  # 우, 하

dp[0][0] = (crops[0][0], crops[0][0])

for i in range(n):
    for j in range(n):
        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                now = dp[i][j]
                crop = crops[nx][ny]
                next = dp[nx][ny]
                dp[nx][ny] = [now[0] + crop,
                              max(now[0] + crop * 2,
                                  now[1] + crop,
                                  next[1])]

print(dp[-1][-1][1])