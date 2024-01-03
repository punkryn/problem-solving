class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        INF = float('inf')
        MOD = 1_000_000_007
        
        graph = [[] for _ in range(n + 1)]
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        
        distance = [INF] * (n + 1)
        distance[n] = 0
        q = [(0, n)]
        ans = [0] * (n + 1)
        ans[n] = 1
        while q:
            cur_cost, cur_node = heapq.heappop(q)
            
            if cur_cost > distance[cur_node]:
                continue
            
            for nxt_node, weight in graph[cur_node]:
                nxt_cost = cur_cost + weight
                
                if nxt_cost < distance[nxt_node]:
                    distance[nxt_node] = nxt_cost
                    heapq.heappush(q, (nxt_cost, nxt_node))
                
                if cur_cost > distance[nxt_node]:
                    ans[cur_node] = (ans[nxt_node] + ans[cur_node]) % MOD

        return ans[1]