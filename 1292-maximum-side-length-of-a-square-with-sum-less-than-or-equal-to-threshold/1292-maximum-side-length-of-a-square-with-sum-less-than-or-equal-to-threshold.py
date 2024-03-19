class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])
        prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                prefix_sum[i + 1][j + 1] = mat[i][j] + prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j]
        
        l, r = 0, min(n, m)

        def deter(mid):
            for i in range(mid, n + 1):
                for j in range(mid, m + 1):
                    comp = prefix_sum[i][j] - prefix_sum[i - mid][j] - prefix_sum[i][j - mid] + prefix_sum[i - mid][j - mid]
                    if comp <= threshold:
                        return True
            return False

        ans = 0
        while l <= r:
            mid = (l + r) // 2

            if deter(mid):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return ans