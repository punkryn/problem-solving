class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        visited = [False] * n
        graph = [[] for _ in range(n)]
        for a, b in richer:
            graph[b].append(a)

        quiet_map = [0] * n
        for i in range(n):
            quiet_map[quiet[i]] = i

        ans = quiet[:]
        def dfs(x):
            if visited[x]:
                return ans[x]
            visited[x] = True
            for nxt in graph[x]:
                ret = dfs(nxt)
                ans[x] = min(ans[x], ret)
            return ans[x]
        
        for i in range(n):
            if visited[i]: continue
            dfs(i)
        return [quiet_map[x] for x in ans]