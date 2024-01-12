class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        l = [0] * n
        r = [0] * n
        
        for i in range(1, n - 1):
            if arr[i - 1] < arr[i]:
                l[i] = l[i - 1] + 1
        
        for i in range(n - 2, 0, -1):
            if arr[i + 1] < arr[i]:
                r[i] = r[i + 1] + 1
        
        ans = 0
        for i in range(1, n - 1):
            if l[i] != 0 and r[i] != 0:
                ans = max(ans, l[i] + r[i] + 1)
        
        return ans