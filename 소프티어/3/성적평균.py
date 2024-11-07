import sys

input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
tree = [0] * (len(s) * 4)

def init(start, end, index):
    if start == end:
        tree[index] = s[start]
        print(start, tree)
        return tree[index]
    mid = (start + end) // 2
    print(start, end, mid, index)
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)

# for _ in range(k):
#
#     l = b - a + 1
#     print(round(sum(s[a-1:b]) / l, 2))

init(0, len(s) - 1, 1)

for _ in range(k):
    a, b = map(int, input().split())
    sum = interval_sum(0, len(s) - 1, 1, a-1, b-1)
    l = b - a + 1
    print(round(sum / l, 2))