from collections import deque

def convert_time(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

def solution(plans):
    result = []

    plans = [(name, convert_time(start), int(playtime)) for name, start, playtime in plans]
    plans.sort(key=lambda x: x[1])

    stops = deque()
    time = 0

    for i in range(len(plans)):
        name, start, playtime = plans[i]

        while stops:
            n, p = stops.pop()
            if time >= p:
                time -= p
                result.append(n)
            else:
                stops.append((n, p - time))
                break

        stops.append((name, playtime))

        if i < len(plans) - 1:
            next_start = plans[i + 1][1]
            time = next_start - start

    while stops:
        n, _ = stops.pop()
        result.append(n)

    return result
