# https://www.acmicpc.net/problem/2630
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dnc(x1, y1, x2, y2):
    global white, blue
    prev = paper[x1][y1]
    flag = False
    for i in range(x1, x2):
        for j in range(y1, y2):
            if paper[i][j] != prev:
                flag = True
                break
        if flag:
            break
    
    if flag:
        dnc(x1, y1, (x1 + x2) // 2, (y1 + y2) // 2)
        dnc(x1, (y1 + y2) // 2, (x1 + x2) // 2, y2)
        dnc((x1 + x2) // 2, y1, x2, (y1 + y2) // 2)
        dnc((x1 + x2) // 2, (y1 + y2) // 2, x2, y2)
    else:
        if prev == 0:
            white += 1
        else:
            blue += 1


if __name__ == '__main__':
    n = int(si())
    paper = [list(mis()) for _ in range(n)]
    
    white = blue = 0
    dnc(0, 0, n, n)
    print(white)
    print(blue)