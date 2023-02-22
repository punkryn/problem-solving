# https://www.acmicpc.net/problem/14500
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

t = {
    'ㅡ': [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)]],
    'ㅁ': [[(0, 1), (1, 0), (1, 1)]],
    'ㄴ': [[(1, 0), (2, 0), (2, 1)], [(1, 0), (0, 1), (0, 2)], [(0, 1), (1, 1), (2, 1)], [(1, 0), (1, -1), (1, -2)], [(1, 0), (2, 0), (2, -1)], [(0, 1), (0, 2), (1, 2)], [(0, 1), (1, 0), (2, 0)], [(1, 0), (1, 1), (1, 2)]],
    'ㄹ': [[(1, 0), (1, 1), (2, 1)], [(0, -1), (1, -1), (1, -2)], [(1, 0), (1, -1), (2, -1)], [(0, 1), (1, 1), (1, 2)]],
    'ㅜ': [[(0, 1), (1, 1), (0, 2)], [(0, 1), (-1, 1), (1, 1)], [(0, 1), (-1, 1), (0, 2)], [(1, 0), (2, 0), (1, 1)]]
}


if __name__ == '__main__':
    n, m = mis()
    board = [list(mis()) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(m):
            for key in t:
                for tet in t[key]:
                    score = board[i][j]
                    for x, y in tet:
                        ni = i + x
                        nj = j + y
                        if not (0 <= ni < n and 0 <= nj < m):
                            break
                        score += board[ni][nj]

                    else:
                        ans = max(ans, score)
    print(ans)