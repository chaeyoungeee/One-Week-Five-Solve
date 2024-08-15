from collections import Counter

def solution(picks, minerals):
    p_sum = sum(picks) * 5
    m_cnts = []
    cnt = 0
    s, e = 0, min(len(minerals), p_sum)
    tired = [(1, 1, 1), (5, 1, 1), (25, 5, 1)] # 피로도
    tired_min = 0

    for i in range(s, e, 5):
        m_cnts.append(Counter(minerals[s:s+5]))
        s += 5
    m_cnts.sort(key=lambda x: (x["diamond"], x["iron"])) # 광물수 기준 내림차순 정렬

    for i, p in enumerate(picks):
        for j in range(0, p):
            if not m_cnts: return tired_min
            m_cnt = m_cnts.pop()
            tired_min += m_cnt["diamond"] * tired[i][0] + m_cnt["iron"] * tired[i][1] + m_cnt["stone"] * tired[i][2]
    return tired_min