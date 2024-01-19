class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)
        ps = [0] * n
        ps[0] = candiesCount[0]
        for i in range(1, n):
            ps[i] = ps[i - 1] + candiesCount[i]
        
        ans = []
        
        for query in queries:
            ft, fd, dc = query
            if ft == 0 and candiesCount[0] > fd:
                ans.append(True)
                continue

            if ps[ft] <= fd:
                ans.append(False)
                continue
            
            if ft > 0 and ps[ft - 1] >= dc * (fd + 1):
                ans.append(False)
                continue
            
            ans.append(True)

        return ans