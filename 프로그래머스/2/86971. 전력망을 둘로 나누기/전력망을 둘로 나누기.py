def solution(n, wires):
    def dfs(x):
        visited.add(x)
        return sum([1] + [dfs(i) for i in tree[x] if i not in visited])
            
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
            
    