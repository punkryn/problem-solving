# https://www.acmicpc.net/problem/2213
import sys
sys.setrecursionlimit(int(1e6))
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def DFS(x, prev):
    use = notUse = 0
    for nxt in tree[x]:
        if nxt == prev: continue
        DFS(nxt, x)
        use += dp[nxt][1]
        notUse += max(dp[nxt])
    
    dp[x][0] = use + w[x]
    dp[x][1] = notUse

def tracking(x, prev, flag):
    if flag:
        ans.append(x)
        for nxt in tree[x]:
            if nxt == prev: continue
            tracking(nxt, x, 0)
    else:
        for nxt in tree[x]:
            if nxt == prev: continue
            tracking(nxt, x, 1 if dp[nxt][0] > dp[nxt][1] else 0)

if __name__ == '__main__':
    n = int(si())
    w = [[0]] + list(mis())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = mis()
        tree[a].append(b)
        tree[b].append(a)
    
    dp = [[0] * 2 for _ in range(n + 1)]
    DFS(1, 0)
    print(max(dp[1]))

    ans = []
    tracking(1, 0, 1 if dp[1][0] > dp[1][1] else 0)
    print(*sorted(ans))