from itertools import combinations as cb
from collections import deque

def solution(coin, cards):
    answer = 1
    n = len(cards)

    init = cards[:n//3]
    idx = 2

    case = list(cb(init, 2))
    cnt = 0
    for i in case:
        if sum(i) == n + 1:
            cnt += 1

    double = []
    while idx <= n-n//3:
        pick = cards[n//3:n//3+idx]

        tcase = list(cb(pick, 2))
        for i in tcase:
            if sum(i) == n + 1:
                double.append(i)

        if coin > 0 :
            if n+1 - pick[-1] in init:
                cnt += 1
                coin -= 1

        if coin > 0 :
            if n+1 - pick[-2] in init:
                cnt += 1
                coin -= 1

        if cnt == 0 :
            if coin >= 2 and len(double) > 0:
                coin -= 2
                double.pop()
                cnt += 1
            else :
                break
        cnt -= 1
        idx += 2
        answer += 1
    return answer