class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cable_cnt = len(connections)

        if cable_cnt < n - 1:
            return -1
        
        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n

        def dfs(x, prev):
            for nxt in graph[x]:
                if nxt == prev: continue
                if visited[nxt]: continue
                visited[nxt] = True
                dfs(nxt, x)
            
        ans = 0
        for i in range(n):
            if visited[i]: continue

            visited[i] = True
            dfs(i, -1)
            ans += 1
        return ans - 1