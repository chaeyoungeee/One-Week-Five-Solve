def solution():
    cnt = 1
    N = int(input())
    grades = list(list(map(int, input().split())) for i in range(N))
    grades = sorted(grades, key=lambda x: (x[0], x[1]))
    max = grades[0][1]

    for i in range(1, len(grades)):
        if grades[i][1] < max:
            cnt += 1
            max = grades[i][1]

    return cnt

T = int(input())

for _ in range(T):
    print(solution())

