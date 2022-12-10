# https://www.acmicpc.net/problem/5875
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

if __name__ == '__main__':
    s = si().strip()

    n = len(s)
    if n % 2 == 1:
        print(0)
        exit()
    
    l = r = total = 0
    ans = 0
    for i in range(n):
        if s[i] == '(':
            l += 1
            total += 1
        else:
            r += 1
            total -= 1
        
        if total == 1:
            l = 0
        
        if total == -1:
            ans = r
            break
    
    if total == 2:
        ans = l
    
    print(ans)