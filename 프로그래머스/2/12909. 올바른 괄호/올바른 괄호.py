def solution(s):
    s = list(s)
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            try:
                if stack.pop() == ')':
                    return False
            except:
                return False
    return False if stack else True