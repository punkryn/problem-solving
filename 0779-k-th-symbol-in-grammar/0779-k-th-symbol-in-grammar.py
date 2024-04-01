class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        k -= 1
        seq = [k]
        for i in range(n):
            k //= 2
            seq.append(k)
        
        cur = '0'
        seq = seq[::-1]
        for i in seq[1:]:
            if cur == '0':
                if i % 2 == 0:
                    cur = '0'
                else:
                    cur = '1'
            else:
                if i % 2 == 0:
                    cur = '1'
                else:
                    cur = '0'
        return int(cur)