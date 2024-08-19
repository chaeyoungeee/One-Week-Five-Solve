import sys

input = sys.stdin.readline
exp = input().split('-')
num = []

for e in exp:
    n = 0
    e = e.split('+')
    for i in e:
        n += int(i)
    num.append(n)

result = num[0] * 2 - sum(num)
print(result)