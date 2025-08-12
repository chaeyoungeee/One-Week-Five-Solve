from collections import defaultdict

def solution(id_list, report, k):
    count = defaultdict(int)
    reporter = defaultdict(set)
    result = []
    
    for r in report:
        p1, p2 = r.split() # 신고자, 피신고자
        reporter[p2].add(p1)
        
    for key in reporter.keys():
        if len(reporter[key]) >= k:
            for r in reporter[key]:
                count[r] += 1

    return [count[uid] for uid in id_list]
        