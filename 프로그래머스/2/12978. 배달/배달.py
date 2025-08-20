import heapq
from collections import defaultdict

def dijkstra(start, maps, distances, visited):
    distances[start] = 0
    pque = [(0, start)] # 비용, 시작점
    
    while pque:
        acost, a = heapq.heappop(pque)
        
        if visited[a]: continue
        visited[start] = 1
        
        for m in maps[a]:
            b, bcost = m
            ncost = acost + bcost
            if distances[b] > ncost:
                distances[b] = ncost
                heapq.heappush(pque, (ncost, b))
    

def solution(N, road, K):
    result = 0
    distances = [int(1e9)] * N
    visited = [0] * N
    maps = defaultdict(list)
    
    for r in road:
        a, b, cost = r
        maps[a-1].append((b-1, cost))
        maps[b-1].append((a-1, cost))
        
    dijkstra(0, maps, distances, visited)
    
    for d in distances:
        if d <= K: result += 1
        
    return result