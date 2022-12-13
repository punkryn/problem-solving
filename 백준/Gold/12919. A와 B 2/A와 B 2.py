# https://www.acmicpc.net/problem/12919
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

def go(length, l, r, flag):
    if length == n:
        if flag == -1:
            if ''.join(T[l:r + 1][::-1]) == S:
                print(1)
                exit()
        else:
            if ''.join(T[l:r + 1]) == S:
                print(1)
                exit()
        return
    
    if flag == 1:
        if T[r] == 'A':
            go(length - 1, l, r - 1, flag)
    else:
        if T[l] == 'A':
            go(length - 1, l + 1, r, flag)

    if flag == 1:
        if T[l] == 'B':
            go(length - 1, l + 1, r, flag * -1)
    else:
        if T[r] == 'B':
            go(length - 1, l, r - 1, flag * -1)

if __name__ == '__main__':
    S = si().strip()
    T = list(si().strip())

    n = len(S)
    m = len(T)

    go(m, 0, m - 1, 1)
    print(0)