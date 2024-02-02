import sys

# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    build = list(mis())
    ans = [0] * n

    for i in range(n - 1):
        prev = (1, -float('inf'))
        for j in range(i + 1, n):
            d = j - i
            h = (build[j] - build[i])

            if prev[1] * d < h * prev[0]:
                prev = (d, h)
                ans[i] += 1

    for i in range(n - 1, 0, -1):
        prev = (1, float('inf'))
        for j in range(i - 1, -1, -1):
            d = i - j
            h = build[i] - build[j]

            if prev[1] * d > h * prev[0]:
                prev = (d, h)
                ans[i] += 1

    print(max(ans))