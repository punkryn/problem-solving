class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        maxChair = 0
        chairQueue = []
        leaving = []
        q = []
        for i in range(len(times)):
            ar, le = times[i]
            heapq.heappush(q, (ar, le, i))

        ans = 0
        while q:
            ar, le, idx = heapq.heappop(q)
            
            while len(leaving) > 0 and leaving[0][0] <= ar:
                curLeave, curChair = heapq.heappop(leaving)
                heapq.heappush(chairQueue, curChair)
            
            if len(chairQueue) == 0:
                heapq.heappush(chairQueue, maxChair)
                maxChair += 1
                
            curChair = heapq.heappop(chairQueue)
            ans = curChair
            heapq.heappush(leaving, (le, curChair))

            if idx == targetFriend:
                break

        return ans