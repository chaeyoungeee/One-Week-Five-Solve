import sys
import itertools
import decimal

def caculate_score(game, r, score):

    i, j = game
    if r == 3:
        score[i] += 3
    elif r == 1:
        score[i] += 1
        score[j] += 1
    else:
        score[j] += 3

def caculate_probability(result):
    p = 1
    for k in range(len(games)):
        i, j = games[k]
        if result[k] == 3:
            p *= (4 * F[i]) / (5 * (F[i] + F[j]))
        elif result[k] == 1:
            p *=  0.2
        else:
            p *= (4 * F[j]) / (5 * (F[i] + F[j]))
    return p


input = sys.stdin.readline
F = list(map(int, input().split()))
games = list(itertools.combinations([0, 1, 2, 3], 2))

probability = 0

# 6번의 경기 결과 (ab, ac, ad, bc, bd, cd)
results = list(itertools.product([3, 1, 0], repeat=6))

for result in results:
    score = [0] * 4
    for i in range(len(games)): # 점수 계산
        caculate_score(games[i], result[i], score)

    a_score = score[0]
    score.sort(reverse=True)

    if a_score >= score[1]:
        p = caculate_probability(result)
        probability += p

decimal.getcontext().rounding = decimal.ROUND_HALF_UP
answer = decimal.Decimal(probability * 100).quantize(decimal.Decimal('1.000'))

print(answer)