class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = d = 0
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for inst in instructions:
            if inst == 'L':
                d = (d + 1) % 4
            elif inst == 'R':
                d = (d - 1) % 4
            else:
                x += dx[d]
                y += dy[d]
        
        return False if (x != 0 or y != 0) and d == 0 else True