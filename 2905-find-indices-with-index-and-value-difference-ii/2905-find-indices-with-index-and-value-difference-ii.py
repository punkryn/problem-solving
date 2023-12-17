class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        min_arr = [[0, _] for _ in range(n)]
        max_arr = [[0, _] for _ in range(n)]
        min_arr[n - 1][0] = nums[n - 1]
        max_arr[n - 1][0] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if min_arr[i + 1][0] < nums[i]:
                min_arr[i][0] = min_arr[i + 1][0]
                min_arr[i][1] = min_arr[i + 1][1]
            else:
                min_arr[i][0] = nums[i]
                min_arr[i][1] = i
            
            if max_arr[i + 1][0] > nums[i]:
                max_arr[i][0] = max_arr[i + 1][0]
                max_arr[i][1] = max_arr[i + 1][1]
            else:
                max_arr[i][0] = nums[i]
                max_arr[i][1] = i
        
        for i in range(n - indexDifference):
            if abs(nums[i] - min_arr[i + indexDifference][0]) >= valueDifference:
                return [i, min_arr[i + indexDifference][1]]
            
            if abs(nums[i] - max_arr[i + indexDifference][0]) >= valueDifference:
                return [i, max_arr[i + indexDifference][1]]
        
        return [-1, -1]