def solution(genres, plays):
    data = {}
    cnt = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] in data:
            d = data[genres[i]]
            d.append((i, plays[i]))
            data[genres[i]] = d
            cnt[genres[i]] += plays[i]
        else:
            data[genres[i]] = [(i, plays[i])]
            cnt[genres[i]] = plays[i]
    for i in data:
        data[i] = sorted(data[i], key=lambda x: (-x[1], x[0]))
    cnt = dict(sorted(cnt.items(), key=lambda x: -x[1]))
    for c in cnt:
        answer.append(data[c][0][0])
        if len(data[c]) > 1:
            answer.append(data[c][1][0])
    return answer