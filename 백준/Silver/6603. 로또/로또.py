from itertools import combinations as cb

def solution(s):
    s.sort()

    combinations = cb(s, 6)

    for c in combinations:
        for i in c:
            print(i, end=" ")
        print()
    print()

while True:
    n = list(map(int, input().split()))
    if n[0] == 0: break
    solution(n[1:])