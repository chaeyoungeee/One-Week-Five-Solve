def solution(targets):
    cur, cnt = 0, 0
    targets.sort(key=lambda x: x[1])
    for t in targets:
        if cur <= t[0]:
            cur = t[1]
            cnt += 1
    return cnt