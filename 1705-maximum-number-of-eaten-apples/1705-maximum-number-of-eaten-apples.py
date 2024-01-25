class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(days)

        ans = 0
        q = []
        for i in range(n):
            apple = apples[i]
            rot = i + days[i]

            if apple > 0:
                heapq.heappush(q, (rot, apple))
            
            while len(q) > 0 and q[0][0] <= i:
                heapq.heappop(q)
            
            if len(q) > 0:
                cur_rot, cur_apple = heapq.heappop(q)
                ans += 1

                if cur_apple > 1:
                    heapq.heappush(q, (cur_rot, cur_apple - 1))
        
        cur_day = n
        while q:
            rot, apple = heapq.heappop(q)
            if rot <= cur_day:
                continue
            
            ans += min(rot - cur_day, apple)
            cur_day += min(rot - cur_day, apple)

        return ans