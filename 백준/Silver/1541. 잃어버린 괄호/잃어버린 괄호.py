import sys
import re

input = sys.stdin.readline
exp = input().split('-')
result = 0

for idx, e in enumerate(exp):
    e = list(map(int, e.split('+')))
    if idx == 0: result += sum(e)
    else: result -= sum(e)

print(result)