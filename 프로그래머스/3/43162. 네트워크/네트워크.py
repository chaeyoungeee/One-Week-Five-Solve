def dfs(graph, visited, v):
    visited[v] = 1
    for i in range(len(graph[v])):
        if not visited[i] and graph[v][i]:
            dfs(graph, visited, i)

def solution(n, computers):
    cnt = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(computers, visited, i)
    return cnt