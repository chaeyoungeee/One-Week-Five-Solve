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
    for i in range(n-1):
        tree = [[] for _ in range(n)]
        visited = set()
        e = (0, 0)
        
        for j in range(n-1):
            if i == j: 
                e = wires[j]
                continue
            a, b = wires[j]
            tree[a-1].append(b-1)
            tree[b-1].append(a-1)
            
        cnt = dfs(e[1]-1)
        result = min(result, abs(n-2*cnt))
        
    return result
            
    