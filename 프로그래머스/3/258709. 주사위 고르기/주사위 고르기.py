from itertools import combinations as cb
from itertools import product as pd

# def solution(dice):
#     l = len(dice)
#     d = list(cb(range(0,l), l//2))
#     l2 = len(d)
#     dl = set()
#     wl = dict()
#     mt = [0, 0]

#     while d:
#         dt = set(range(0, l)) - set(d.pop())
#         if dt not in dl:
#             dl.add(tuple(dt))
#         if len(dl) == (l2 // 2):
#             break
    
#     for i in dl:
#         dt = set(range(0, l)) - set(i)
#         product1 = list(pd(*[dice[j] for j in i]))
#         product2 = list(pd(*[dice[j] for j in dt]))
    
#         sum1 = [sum(p) for p in product1]
#         sum2 = [sum(p) for p in product2]
        
#         product3 = list(pd(sum1, sum2))
        
#         cnt = [0, 0, 0]
#         for p in product3:
#             if p[0] > p[1]:
#                 cnt[0] += 1
#             elif p[0] < p[1]:
#                 cnt[2] += 1
#             else:
#                 cnt[1] += 1
#         wl[frozenset(i)] = cnt
    
#     for key, value in wl.items():
#         if mt[1] < value[0]:
#             mt[0], mt[1] = key, value[0]
#         if mt[1] < value[2]:
#             mt[0], mt[1] = set(range(0, l)) - key, value[2]
    
#     return [i + 1 for i in mt[0]]
        
def solution(dice):
    l = len(dice)
    d = list(cb(range(0, l), l // 2))  # A와 B로 나눌 수 있는 조합
    l2 = len(d)
    dl = set()
    wl = dict()
    mt = [0, 0]
    
    while d:
        dt = set(range(0, l)) - set(d.pop())
        if dt not in dl:
            dl.add(tuple(dt))
        if len(dl) == (l2 // 2):
            break
    
    for i in dl:
        dt = set(range(0, l)) - set(i)
        
        product1 = list(pd(*[dice[j] for j in i]))  # A의 경우의 수
        product2 = list(pd(*[dice[j] for j in dt])) # B의 경우의 수
    
        sum1 = [sum(p) for p in product1]  # A의 점수 합
        sum2 = [sum(p) for p in product2]  # B의 점수 합
        
        # A와 B의 점수 비교
        cnt = [0, 0, 0]
        for a_sum in sum1:
            for b_sum in sum2:
                if a_sum > b_sum:
                    cnt[0] += 1  # A 승리
                elif a_sum < b_sum:
                    cnt[2] += 1  # B 승리
                else:
                    cnt[1] += 1  # 무승부
        
        wl[frozenset(i)] = cnt
    
    # 승리 확률이 가장 높은 조합 찾기
    for key, value in wl.items():
        if mt[1] < value[0]:
            mt[0], mt[1] = key, value[0]
        if mt[1] < value[2]:
            mt[0], mt[1] = set(range(0, l)) - key, value[2]
    
    return sorted([i + 1 for i in mt[0]])  # 주사위 번호는 1부터 시작하므로 +1