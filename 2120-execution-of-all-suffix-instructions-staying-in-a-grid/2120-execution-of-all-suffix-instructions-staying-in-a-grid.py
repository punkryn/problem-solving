class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        ans = [0] * m

        d = {
            'R': [0, 1],
            'L': [0, -1],
            'U': [-1, 0],
            'D': [1, 0],
        }

        def check(x, y):
            if not (0 <= x < n and 0 <= y < n):
                return False
            return True

        for i in range(m):
            sx, sy = startPos
            cnt = 0
            for j in range(i, m):
                w = s[j]
                dx, dy = d[w]
                sx += dx
                sy += dy
                if not check(sx, sy):
                    break
                cnt += 1
            ans[i] = cnt
        
        return ans