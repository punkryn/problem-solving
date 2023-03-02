# https://www.acmicpc.net/problem/19949
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(depth):
    global ans
    if depth == 10:
        cnt = 0
        for i in range(10):
            if prev[i] == a[i]:
                cnt += 1
        ans = ans + (1 if cnt >= 5 else 0)
        return
    
    for i in range(1, 6):
        if depth > 1 and prev[depth - 1] == i and  prev[depth - 2] == i:
            continue
        
        prev[depth] = i
        go(depth + 1)
        prev[depth] = 0

if __name__ == '__main__':
    a = list(mis())
    prev = [0] * 10
    ans = 0
    go(0)
    print(ans)