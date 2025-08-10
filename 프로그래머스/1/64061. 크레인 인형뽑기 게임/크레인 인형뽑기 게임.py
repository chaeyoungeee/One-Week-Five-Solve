def solution(board, moves):
    count = 0
    stack = []
    
    for y in moves:
        y -= 1
        for x in range(len(board)):
            v = board[x][y]
            if v != 0:
                if stack and (stack[-1] == v):
                    stack.pop()
                    count += 2
                else:
                    stack.append(v)       
                board[x][y] = 0
                break
    
    return count