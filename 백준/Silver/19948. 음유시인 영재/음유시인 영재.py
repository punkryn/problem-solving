# https://www.acmicpc.net/problem/19948
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(p):
    global n
    alpha[ord(p[0].upper()) - ord('A')] -= 1
    if alpha[ord(p[0].upper()) - ord('A')] == -1:
        print(-1)
        exit()
    for i in range(1, len(p)):
        if p[i] == p[i - 1]:
            continue

        if p[i] == ' ':
            if n == 0:
                print(-1)
                exit()
            n -= 1
            continue


        if alpha[ord(p[i].upper()) - ord('A')] == 0:
            print(-1)
            exit()

        alpha[ord(p[i].upper()) - ord('A')] -= 1

if __name__ == '__main__':
    p = si().strip()
    n = int(si())
    alpha = list(mis())
    
    check(p)
    
    title = ''.join([row[0].upper() for row in p.split()])
    check(title)
    print(title)