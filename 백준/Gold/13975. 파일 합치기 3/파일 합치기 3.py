# https://www.acmicpc.net/problem/13975
import sys
from heapq import heappush, heappop, heapify
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

if __name__ == '__main__':
    for _ in range(int(si())):
        k = int(si())
        files = list(mis())
        heapify(files)

        ans = 0
        while len(files) > 1:
            x = heappop(files)
            y = heappop(files)

            ans = ans + x + y
            
            heappush(files, x + y)
        print(ans)