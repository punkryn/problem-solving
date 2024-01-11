class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0: return False

        p = s // k

        if max(nums) > p: return False

        n = len(nums)
        nums.sort()
        v = [False] * n
        def go(depth, cur, idx):
            if depth == k:
                if False in v:
                    return False
                return True

            if cur == p:
                return go(depth + 1, 0, 0)

            ret = False
            for i in range(idx, n):
                if v[i]: continue
                nxt = cur + nums[i]
                if nxt > p: break
                
                v[i] = True
                ret |= go(depth, nxt, i + 1)
                if ret: return ret
                v[i] = False

            return ret
        
        return go(0, 0, 0)