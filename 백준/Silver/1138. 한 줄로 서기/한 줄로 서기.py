n = int(input())
data = list(map(int, input().split()))
result = [0] * n

for i in range(len(data)):
    cnt = 0
    for j in range(len(result)):
        if cnt == data[i] and result[j] == 0:
            result[j] = i + 1
            break
        if result[j] == 0:
            cnt += 1

print(*result)
