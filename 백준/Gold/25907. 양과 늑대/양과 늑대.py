# https://www.acmicpc.net/problem/25907
import sys
si = sys.stdin.readline
flush = sys.stdout.flush
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())

    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        
        print(f'? {mid}')
        flush()
        s = int(si())
        w = mid - s

        if s == w:
            print(f'! {mid}')
            break
        elif s < w:
            r = mid - 1
        else:
            l = mid + 1