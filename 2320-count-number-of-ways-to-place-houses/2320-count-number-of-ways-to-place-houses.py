class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = int(1e9) + 7
        a = b = 1
        
        for i in range(1, n):
            c = b
            b += a
            a = c
        
        return ((a + b) ** 2) % MOD