class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0: return -1

        d = str(k)[-1]
        if d != '1' and d != '3' and d != '7' and d != '9':
            return -1
        
        f = self.getFirst(k)
        ans = len(str(f))
        prev = -1
        prev_mod = -1
        while f % k != 0:
            mok = f // k
            mod = f % k
            if prev == mok and prev_mod == mod:
                return -1
            prev = mok
            prev_mod = mod
            nxt = mod * 10 + 1
            if nxt < k:
                nxt = nxt * 10 + 1
                ans += 1
            ans += 1
            f = nxt

        return ans
        
    def getFirst(self, n):
        s = str(n)
        length = len(s)

        c = '1' * length
        
        if int(c) < n:
            return int(c + '1')
        
        return int(c)