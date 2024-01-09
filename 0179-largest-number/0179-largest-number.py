class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(a, b):
            c = a + b
            d = b + a
            
            for i in range(len(c)):
                if c[i] == d[i]:
                    continue
                
                if c[i] > d[i]:
                    return -1

                return 1    
            return 0
        
        ans = ''.join(sorted(map(str, nums), key=cmp_to_key(comp)))
        return ans if ans[0] != '0' else '0'
