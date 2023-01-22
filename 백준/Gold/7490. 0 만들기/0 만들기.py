# https://www.acmicpc.net/problem/7490
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(depth, v):
    if depth == n:
        v.append(str(n))
        s = ''
        for i in v:
            if i == ' ':
                continue
            s += i
        if eval(s) == 0:
            ans.append(''.join(v))
        v.pop()
        return        
    
    for w in ['+', ' ', '-']:
        v.append(str(depth))
        v.append(w)
        go(depth + 1, v)
        v.pop()
        v.pop()

if __name__ == '__main__':
    for _ in range(int(si())):
        n = int(si())

        ans = []
        go(1, [])

        for a in sorted(ans):
            print(a)

        print()