# https://www.acmicpc.net/problem/2661
import sys
si = sys.stdin.readline

def check(seq):
    l = len(seq)
    for i in range(1, l // 2 + 1):
        if l % 2 == 1:
            for j in range(l - i + 1):
                if seq[j: j + i] == seq[j + i: j + i + i]:
                    return True
        else:
            for j in range(l - i):
                if seq[j: j + i] == seq[j + i: j + i + i]:
                    return True
    return False

def go(depth, prev, cur=''):
    if depth == n:
        print(int(cur))
        exit()
    
    for i in ['1', '2', '3']:
        if i == prev: continue
        if check(cur + i): continue
        go(depth + 1, i, cur + i)

if __name__ == '__main__':
    n = int(si())
    go(0, 0)
