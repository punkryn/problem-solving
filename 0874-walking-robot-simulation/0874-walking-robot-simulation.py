dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obsSet = set([(y, x) for x, y in obstacles])
        curDirection = 0
        curX, curY = 0, 0
        ans = 0
        for command in commands:
            if command == -1:
                curDirection = (curDirection + 1) % 4
                continue
            
            if command == -2:
                curDirection = (curDirection - 1) % 4
                continue
            
            for i in range(command):
                nx, ny = curX + dx[curDirection], curY + dy[curDirection]
                if (nx, ny) in obsSet:
                    break

                curX, curY = nx, ny
            
            ans = max(ans, curX ** 2 + curY ** 2)
            
        return ans