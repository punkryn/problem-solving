# https://www.acmicpc.net/problem/25971
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())
dx = [-1, 0, 1, 0, 0]
dy = [0, 1, 0, -1, 0]

if __name__ == '__main__':
    n, k, r, q = mis()
    
    route = [(float('inf'), float('inf'), 4)] * (n + 1)
    
    a = [tuple(mis()) for _ in range(k)]

    for i in range(k - 1):
        d1, x1, y1 = a[i]
        d2, x2, y2 = a[i + 1]

        if x1 == x2 and y1 == y2: d = 4
        elif x1 > x2 and y1 == y2: d = 0
        elif x1 < x2 and y1 == y2: d = 2
        elif x1 == x2 and y1 > y2: d = 3
        else: d = 1

        x_, y_ = x1, y1
        for j in range(d1, d2):
            route[j] = (x_, y_, d)
            x_ += dx[d]
            y_ += dy[d]
    
    route[n] = (x_, y_, d)

    for i in range(q):
        j, xj, yj = mis()
        x1, y1, d = route[j]
        dist = (x1 - xj) ** 2 + (y1 - yj) ** 2
        r1 = r ** 2

        if dist > r1:
            print('gori')
            continue

        if d == 2:
            if yj == y1:
                print('gori')
            elif yj > y1:
                print('safe')
            else:
                print('unsafe')
        elif d == 0:
            if yj == y1:
                print('gori')
            elif yj > y1:
                print('unsafe')
            else:
                print('safe')
        elif d == 1:
            if xj == x1:
                print('gori')
            elif xj < x1:
                print('safe')
            else:
                print('unsafe')
        elif d == 3:
            if xj == x1:
                print('gori')
            elif xj < x1:
                print('unsafe')
            else:
                print('safe')
            