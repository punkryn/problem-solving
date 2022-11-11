# https://www.acmicpc.net/problem/25945
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    a = sorted(mis(), reverse=True)

    SUM = sum(a)
    avg = SUM // n
    remain = SUM % n
    
    ans = 0
    for i in range(remain):
        if a[i] <= avg: break
        ans += a[i] - avg - 1
    for i in range(remain, n):
        if a[i] <= avg: break
        ans += a[i] - avg
    print(ans)