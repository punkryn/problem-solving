class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        
        if a + b < c:
            return a + b
        
        # # 43 - 25 = 18 -> 9
        # # 25, 24 -> 24
        # # 24 + 9 = 33
        # if (a + b - c) % 2 != 0:
        #     d = min((a + b - c) // 2, a)
        #     return min(a + b - d * 2, c) + d
    
        return (a + b - c) // 2 + c