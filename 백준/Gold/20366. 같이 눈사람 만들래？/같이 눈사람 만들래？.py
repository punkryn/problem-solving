# https://www.acmicpc.net/problem/20366
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    H = list(mis())
    comb = sorted([(H[i] + H[j], i, j) for i in range(n - 1) for j in range(i + 1, n)])

    ans = INF
    for l in range(len(comb) - 1):
        hl, il, jl = comb[l]
        for r in range(l + 1, len(comb)):
            hr, ir, jr = comb[r]

            if il not in [ir, jr] and jl not in [ir, jr]:
                ans = min(ans, hr - hl)
                break
        
    print(ans)