import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    a, b, c = mis()
    cnt = [0] * 7
    cnt[a] += 1; cnt[b] += 1; cnt[c] += 1
    count = max(cnt)
    for i in range(6, 0, -1):
        if cnt[i] == count:
            if count == 3:
                print(10000 + i * 1000)
            elif count == 2:
                print(1000 + i * 100)
            else:
                print(i * 100)
            break