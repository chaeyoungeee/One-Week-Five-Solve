def solution(brown, yellow):
    s = 0
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            y = yellow // i
            b = (y + 2) * (i + 2) - yellow
            if b == brown:
                s = y
                break
    return [s+2, yellow//s+2]