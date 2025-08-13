def solution(enroll, referral, seller, amount):
    m = { e: 0 for e in enroll }
    r = { e: r for e, r in zip(enroll, referral) }
    
    for s, a in zip(seller, amount):
        a = a * 100
        while True:
            a2 = a // 10
            a1 = a - a2
            m[s] += a
            if a2 < 1: break
            else:
                m[s] -= a2
                if r[s] == '-': break
                a = a2
                s = r[s]
    
    return [ i[1] for i in m.items() ]
            