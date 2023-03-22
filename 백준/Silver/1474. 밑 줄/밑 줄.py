# https://www.acmicpc.net/problem/1474
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = mis()
    words = [si().strip() for _ in range(n)]
    l = sum([len(word) for word in words]) + n - 1

    d = m - l
    
    mok = d // (n - 1)
    na = d % (n - 1)
    
    ans = words[0]
    for idx, word in enumerate(words[1:], start=1):
        if word[0] > '_':
            line = '_' * (1 + mok + (1 if na > 0 else 0))
            na -= 1
        else:
            if n - idx == na:
                line = '_' * (1 + mok + 1)
                na -= 1
            else:
                line = '_' * (1 + mok)
        
        ans += line + word
    print(ans)