# https://www.acmicpc.net/problem/25312
import sys
import math
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n, m = mis()
    wv = sorted([list(mis()) for _ in range(n)], key=lambda x: x[1] / x[0], reverse=True)
    
    total = 0
    bj = 0
    bm = 1
    for w, v in wv:
        if total == m: break
        
        remain = m - total
        if remain >= w:
            total += w
            bj += v
        else:
            total = m
            bm *= w
            bj *= bm
            bj += remain * v
    gcd = math.gcd(bj, bm)
    bj //= gcd
    bm //= gcd
    print(f'{bj}/{bm}')