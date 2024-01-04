class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        MAX_N = 1005
        matrix = [[''] * MAX_N for _ in range(MAX_N)]

        x, y = 0, 0
        flag = 0
        cnt = 0

        while cnt < len(s):
            matrix[x][y] = s[cnt]

            if flag == 0:
                x += 1
            else:
                x -= 1
                y += 1
        
            cnt += 1
            if cnt % (numRows - 1) == 0:
                flag = (flag + 1) % 2
        
        return ''.join([''.join(mat) for mat in matrix[:numRows]])