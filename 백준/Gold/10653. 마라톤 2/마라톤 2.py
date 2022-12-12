# https://www.acmicpc.net/problem/10653
import sys
from heapq import heappush, heappop
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, k = mis()
    points = [list(mis()) for _ in range(n)]

    q = [(0, 0, 0)]
    dist = [[INF] * (k + 1) for _ in range(n)]
    dist[0][0] = 0

    while q:
        cur_dist, cur, cnt = heappop(q)

        # if cur_dist == n - 1:
        #     break

        if cur_dist > dist[cur][cnt]: continue

        nxt = cur + 1
        if nxt < n:
            nxt_dist = cur_dist + abs(points[nxt][0] - points[cur][0]) + abs(points[nxt][1] - points[cur][1])
            if nxt_dist < dist[nxt][cnt]:
                dist[nxt][cnt] = nxt_dist
                heappush(q, (nxt_dist, nxt, cnt))

        for i in range(2, k + 1):
            nxt = cur + i
            nxt_cnt = cnt + i - 1
            if nxt >= n: break
            if nxt_cnt > k: break
            
            nxt_dist = cur_dist + abs(points[nxt][0] - points[cur][0]) + abs(points[nxt][1] - points[cur][1])
            
            if nxt_dist < dist[nxt][nxt_cnt]:
                dist[nxt][nxt_cnt] = nxt_dist
                heappush(q, (nxt_dist, nxt, nxt_cnt))
    
    print(min(dist[n - 1]))