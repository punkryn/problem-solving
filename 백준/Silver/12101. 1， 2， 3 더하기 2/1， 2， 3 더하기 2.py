# https://www.acmicpc.net/problem/12101
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def go(cur, SUM):
    global order
    if SUM == n:
        order += 1
        if order == k:
            print('+'.join(map(str, cur)))
            exit()
        return
    
    for x in [1, 2, 3]:
        if SUM + x > n: break
        cur.append(x)
        go(cur, SUM + x)
        cur.pop()

if __name__ == '__main__':
    n, k = mis()
    order = 0
    go([], 0)
    print(-1)