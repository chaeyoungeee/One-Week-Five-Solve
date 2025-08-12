from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    result = []
    for c in course:
        menus = defaultdict(int)
        for order in orders:
            order = sorted(order)
            combs = list(combinations(order, c))
            for comb in combs:
                menus["".join(comb)] += 1
        menus = sorted(menus.items(), key=lambda x: -x[1])
        
        for menu in menus:
            if menu[1] < 2: break
            if menu[1] != menus[0][1]: break
            result.append(menu[0])
            
    return sorted(result)