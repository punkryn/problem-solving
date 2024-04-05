class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        n = 3
        x_cnt = sum([1 for i in range(n) for j in range(n) if board[i][j] == 'X'])
        o_cnt = sum([1 for i in range(n) for j in range(n) if board[i][j] == 'O'])

        if not (x_cnt - o_cnt == 0 or x_cnt - o_cnt == 1):
            return False
        
        x_complete = 0
        o_complete = 0
        for i in range(n):
            if board[i].count('X') == n:
                x_complete += 1
            if board[i].count('O') == n:
                o_complete += 1

        for i in range(n):
            for j in range(n):
                if board[j][i] != 'X':
                    break
            else:
                x_complete += 1

        for i in range(n):
            for j in range(n):
                if board[j][i] != 'O':
                    break
            else:
                o_complete += 1
        
        for i in range(n):
            if board[i][i] != 'X':
                break
        else:
            x_complete += 1

        for i in range(n):
            if board[i][i] != 'O':
                break
        else:
            o_complete += 1

        for i in range(n):
            if board[i][n - i - 1] != 'X':
                break
        else:
            x_complete += 1

        for i in range(n):
            if board[i][n - i - 1] != 'O':
                break
        else:
            o_complete += 1
        
        if x_complete != 0 and o_complete != 0:
            return False

        if x_complete != 0:
            if x_cnt == o_cnt:
                return False
        
        if o_complete != 0:
            if x_cnt > o_cnt:
                return False

        return True