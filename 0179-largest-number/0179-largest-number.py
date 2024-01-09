class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(a, b):
            if a + b > b + a:
                return -1
            return 1
        
        ans = ''.join(sorted(map(str, nums), key=cmp_to_key(comp)))
        return ans if ans[0] != '0' else '0'
