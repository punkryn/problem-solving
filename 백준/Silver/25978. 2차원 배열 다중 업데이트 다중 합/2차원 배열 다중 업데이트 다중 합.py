# https://www.acmicpc.net/problem/25978
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n, m = mis()
    aa = [list(mis()) + [0] for _ in range(n)] + [[0] * (n + 1)]

    a = [[0] * (n + 1) for _ in range(n + 1)]
    
    flag = True
    for _ in range(m):
        query = list(mis())

        if query[0] == 1:
            _, i1, j1, i2, j2, k = query

            a[i1][j1] += k
            a[i1][j2 + 1] -= k
            a[i2 + 1][j1] -= k
            a[i2 + 1][j2 + 1] += k
        else:
            if flag:
                flag = False
                for i in range(n):
                    for j in range(1, n):
                        a[i][j] += a[i][j - 1]
                for j in range(n):
                    for i in range(1, n):
                        a[i][j] += a[i - 1][j]
                
                for i in range(n):
                    for j in range(n):
                        a[i][j] += aa[i][j]

                for i in range(n):
                    for j in range(1, n):
                        a[i][j] += a[i][j - 1]
                for j in range(n):
                    for i in range(1, n):
                        a[i][j] += a[i - 1][j]

            _, i1, j1, i2, j2 = query

            print(a[i2][j2] - (a[i2][j1 - 1] if j1 - 1 >= 0 else 0) - (a[i1 - 1][j2] if i1 - 1 >= 0 else 0) + (a[i1 - 1][j1 - 1] if i1 - 1 >= 0 and j1 - 1 >= 0 else 0))
