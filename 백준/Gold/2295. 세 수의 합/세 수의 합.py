# https://www.acmicpc.net/problem/2295
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    U = set([int(si()) for _ in range(n)])

    t = set()
    for a in U:
        for b in U:
            t.add(a + b)
    
    ans = 0
    for a in U:
        for b in U:
            if b > a: continue
            if a - b in t:
                ans = max(ans, a)
    print(ans)