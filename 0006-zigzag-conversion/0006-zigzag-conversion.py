class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ans = [''] * numRows
        bias = (numRows - 1) * 2
        for i in range(len(s)):
            mod = i % bias
            if mod >= numRows:
                ans[bias - mod] += s[i]
                continue
            ans[mod] += s[i]
        return ''.join(ans)