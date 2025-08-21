from pprint import pprint

def solution(n, wires):
    def dfs(x):
        cnt = 1
        visited.add(x)
        for i in tree[x]:
            if i not in visited:
                cnt += dfs(i)
        return cnt
            
    result = n 
    tree = [[] for _ in range(n + 1)]
    
    for i in range(n-1):
        a, b = wires[i]
        
        tree[a].append(b)
        tree[b].append(a)
        
    for i in range(n-1):
        visited = set()
        a, b = wires[i]
        visited.add(b)
        result = min(result, abs(n-2*dfs(a)))
        
    return result
            
    