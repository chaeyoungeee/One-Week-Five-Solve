from collections import deque
from pprint import pprint

def solution(board):
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    n = len(board)
    result = 1e9

    costs = [[1e9] * n for _ in range(n)]
    costs[0][0] = 0
    
    que = deque([(0, 0, d, 0) for d in ['D', 'R']])
    
    while que:
        x, y, d, cost = que.popleft()
        for k, v in directions.items():
            nx, ny = x + v[0], y + v[1]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if board[nx][ny]: continue
            
            new_cost = cost + 100
            if d != k: new_cost += 500
            
            if costs[nx][ny] and costs[nx][ny] + 600 < new_cost + 200: continue
            
            costs[nx][ny] = new_cost
            que.append((nx, ny, k, new_cost))
            
            if costs[n-1][n-1]:
                result = min(result, costs[n-1][n-1])
            

    return result
    
            