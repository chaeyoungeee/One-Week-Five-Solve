def solution(enroll, referral, seller, amount):
    m = { e: 0 for e in enroll }
    r = dict(zip(enroll, referral))
    
    for s, a in zip(seller, amount):
        a = a * 100
        while a > 0 and s != "-":
            m[s] += (a - a // 10)
            a //= 10
            s = r[s]
    
    return [ m[e] for e in enroll ]
            