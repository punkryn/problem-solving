class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [0] * n

        def dfs(x, prev):
            if x == destination:
                return True

            ret = False
            for nxt in graph[x]:
                if prev == nxt:
                    continue
                
                if visited[nxt] == 1:
                    continue
                
                visited[nxt] = 1
                ret |= dfs(nxt, x)
                if ret: return True
            return ret
        
        visited[source] = 1
        return dfs(source, -1)