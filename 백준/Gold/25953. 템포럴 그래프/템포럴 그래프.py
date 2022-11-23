# https://www.acmicpc.net/problem/25953
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n, t, m = mis()
    s, e = mis()
    
    dist = [float('inf')] * n
    dist[s] = 0
    
    for i in range(1, t + 1):
        nxt = dist[:]
        for j in range(m):
            a, b, w = mis()
            nxt[b] = min(nxt[b], dist[a] + w)
            nxt[a] = min(nxt[a], dist[b] + w)
        dist = nxt
    
    print(dist[e] if dist[e] != float('inf') else -1)