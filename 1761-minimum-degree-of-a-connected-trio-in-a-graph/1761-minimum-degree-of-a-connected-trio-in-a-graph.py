class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = [[0] * (n + 1) for _ in range(n + 1)]
        degree = [0] * (n + 1)
        
        for u, v in edges:
            graph[u][v] = 1
            graph[v][u] = 1
            degree[u] += 1
            degree[v] += 1
        
        ans = float('inf')
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if graph[i][j] != 1: continue
                for k in range(1, n + 1):
                    if graph[i][k] == 1 and graph[j][k] == 1:
                        ans = min(ans, degree[i] + degree[j] + degree[k] - 6)
                    
        return ans if ans != float('inf') else -1