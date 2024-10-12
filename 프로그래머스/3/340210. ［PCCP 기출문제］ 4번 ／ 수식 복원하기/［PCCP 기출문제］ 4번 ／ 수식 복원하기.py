from collections import deque

def convert_to_decimal(b, n):
    num = 0
    for j in range(len(n)):
        num += (b ** (len(n) - 1 - j)) * int(n[j])
    return num

def convert_from_decimal(b, n):
    num = deque([])
    n = int(n)
    while b <= n: 
        r = n % b
        n //= b
        num.appendleft(str(r))
    num.appendleft(str(n))
    return int(''.join(num))

def calculate(a, b, operator):
    if operator == '+': return a + b
    else: return a - b

def solution(expressions):
    base = set()
    m = 2
    exp = []
    exp2 = []
    result = []
    for e in expressions:
        s = list(e.split(' '))
        for i in s[0]:
            m = max(m, int(i)+1)
        for i in s[2]:
            m = max(m, int(i)+1)
    
        if s[4] == 'X':
            exp2.append(s)
        else:
            for i in s[4]:
                m = max(m, int(i)+1)
            exp.append(s)     

    if m != 9:
        for i in range(m, 10): base.add(i)
        for e in exp:
            for i in range(m, 10):
                a = convert_to_decimal(i, e[0])
                b = convert_to_decimal(i, e[2])
                c = convert_to_decimal(i, e[4])
                if calculate(a, b, e[1]) != c: 
                    base.discard(i)
    else:
        base.add(m)
        
    if len(base) == 1:
        ba = base.pop()
        for e in exp2:
            a = convert_to_decimal(ba, e[0])
            b = convert_to_decimal(ba, e[2])
            e[4] = str(convert_from_decimal(ba, calculate(a, b, e[1])))
            result.append(' '.join(e))
        return result
    else:
        for e in exp2:
            v = -1
            for ba in base:
                a = convert_to_decimal(ba, e[0])
                b = convert_to_decimal(ba, e[2])
                c = str(convert_from_decimal(ba, calculate(a, b, e[1])))
                print(ba,a,b,c)
                if v == -1: v = c
                else:
                    if v != c:
                        e[4] = '?'
                        result.append(' '.join(e))
                        break
            else:
                e[4] = v
                result.append(' '.join(e))
            
    return result
                        
            

