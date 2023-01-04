# https://www.acmicpc.net/problem/15659
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(depth, cur):
    global maxv, minv
    if depth == n - 1:
        tmp = eval(cur)
        maxv = max(maxv, tmp)
        minv = min(minv, tmp)
        return
    
    if cnt[0]:
        cnt[0] -= 1
        go(depth + 1, cur + '+' + str(A[depth + 1]))
        cnt[0] += 1
    
    if cnt[1]:
        cnt[1] -= 1
        go(depth + 1, cur + '-' + str(A[depth + 1]))
        cnt[1] += 1
    
    if cnt[2]:
        cnt[2] -= 1
        go(depth + 1, cur + '*' + str(A[depth + 1]))
        cnt[2] += 1
    
    if cnt[3]:
        cnt[3] -= 1
        go(depth + 1, cur + '//' + str(A[depth + 1]))
        cnt[3] += 1

if __name__ == '__main__':
    n = int(si())
    A = list(mis())
    cnt = list(mis())

    maxv = -INF
    minv = INF
    
    go(0, str(A[0]))
    print(maxv)
    print(minv)