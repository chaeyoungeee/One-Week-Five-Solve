import sys
import re

input = sys.stdin.readline
exp = re.split(r'(\+|\-)', input().strip())
minus, sum = 0, int(exp[0])

for i in range(1, len(exp), 2): # 홀수번만
    next = int(exp[i + 1])
    if exp[i] == '+':
        if minus == 0:
            sum += next
        else:
            minus += next
    else:
        if minus == 0:
            minus += next
        else:
            sum -= minus
            minus = next
sum -= minus

print(sum)