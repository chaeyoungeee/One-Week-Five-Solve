def solution(board):
    n, m = len(board), len(board[0])
    ans = 0
    
    if n <= 1 or m <= 1:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1: return 1
        
    
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min([board[i-1][j], board[i-1][j-1], board[i][j-1]]) + 1
                ans = max(board[i][j], ans)

    return ans**2
        
        