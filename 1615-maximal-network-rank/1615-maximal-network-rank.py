class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]
        for x, y in roads:
            graph[x].add(y)
            graph[y].add(x)
        
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans = max(ans, len(graph[i]) + len(graph[j]) - (1 if i in graph[j] else 0))

        return ans