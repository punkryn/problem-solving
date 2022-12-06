# https://www.acmicpc.net/problem/14476
import sys
from math import gcd
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

if __name__ == '__main__':
    n = int(si())
    a = [0] + list(mis())

    l = [0] * (n + 1)
    r = [0] * (n + 1)
    
    l[0] = a[1]
    for i in range(1, n + 1):
        l[i] = gcd(l[i - 1], a[i])
    
    r[n] = a[n]
    for i in range(n - 1, 0, -1):
        r[i] = gcd(r[i + 1], a[i])
    
    ans = 0
    ans_num = 0
    for i in range(1, n + 1):
        if i == 1:
            tmp = r[i + 1]
        elif i == n:
            tmp = l[i - 1]
        else:
            tmp = gcd(l[i - 1], r[i + 1])
        if ans < tmp and a[i] % tmp != 0:
            ans = tmp
            ans_num = a[i]
    
    if ans_num == 0:
        print(-1)
    else:
        print(ans, ans_num)