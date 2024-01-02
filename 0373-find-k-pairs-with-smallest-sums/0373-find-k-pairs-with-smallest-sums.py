class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = []
        for x in nums1[:k]:
            heapq.heappush(q, (x + nums2[0], (x, nums2[0]), 0))
        
        ans = []
        while k:
            x, y, idx = heapq.heappop(q)

            ans.append([y[0], y[1]])
            if idx + 1 >= len(nums2):
                k -= 1
                continue

            heapq.heappush(q, (y[0] + nums2[idx + 1], (y[0], nums2[idx + 1]), idx + 1))

            k -= 1
        return ans