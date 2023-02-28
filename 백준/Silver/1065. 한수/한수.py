# https://www.acmicpc.net/problem/1065
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    
    cnt = 0
    for i in range(1, n + 1):
        s = str(i)
        if len(s) == 1:
            cnt += 1
        else:
            prev = int(s[1]) - int(s[0])
            flag = False
            for j in range(2, len(s)):
                d = int(s[j]) - int(s[j - 1])
                if prev != d:
                    flag = True
                    break
            
            if not flag:
                cnt += 1
    print(cnt)