from heapq import heappush, heappop

INF = 10**9
def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n + 1)]
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)
    
    dist = [INF] * (n + 1)
    dist[destination] = 0
    q = [(0, destination)]
    while q:
        cur_dist, cur = heappop(q)
        
        if cur_dist > dist[cur]:
            continue
        
        for nxt in graph[cur]:
            nxt_dist = cur_dist + 1
            if nxt_dist < dist[nxt]:
                dist[nxt] = nxt_dist
                heappush(q, (nxt_dist, nxt))
    
    for s in sources:
        if dist[s] == INF:
            answer.append(-1)
        else:
            answer.append(dist[s])
    return answer