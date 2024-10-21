n = int(input())
s_list = list(map(int, input().split()))
s_list.sort()

print(s_list[-1]+n-1)