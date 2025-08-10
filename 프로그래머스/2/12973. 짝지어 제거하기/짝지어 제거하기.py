def solution(s):
    stack = []

    for k in s:
        if stack and stack[-1] == k:
            stack.pop()
        else:
            stack.append(k)
    
    return 0 if stack else 1