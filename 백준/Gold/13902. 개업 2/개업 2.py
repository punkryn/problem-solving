# https://www.acmicpc.net/problem/13902
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

if __name__ == '__main__':
    n, m = mis()
    S = list(mis()) + [0]

    cand = set()
    for i in range(m):
        for j in range(i + 1, m + 1):
            cand.add(S[i] + S[j])
    
    dp = [INF] * (n + 1)
    dp[0] = 0
    for i in range(n):
        for j in cand:
            nxt = i + j
            if nxt > n: continue
            dp[nxt] = min(dp[nxt], dp[i] + 1)
    
    print(dp[n] if dp[n] != INF else -1)