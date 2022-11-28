# https://www.acmicpc.net/problem/16226

import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

DD = 0
MIRROR = 1

class Node:
    def __init__(self, flag, v):
        self.flag = flag
        self.l = None
        self.r = None
        self.v = v
        self.end = False

LIMIT = 10**5 + 10
if __name__ == '__main__':
    n = int(si())
    row = [dict() for _ in range(LIMIT)]

    ops = [list(mis()) for _ in range(n)]
    nodes = dict()
    for x, y in ops:
        dd = Node(DD, (x, y))
        mirror = Node(MIRROR, (x + 1, y))
        row[x][y] = dd
        row[x + 1][y] = mirror
        nodes[(x, y)] = dd
        nodes[(x + 1, y)] = mirror
    
    for i in range(1, LIMIT):
        col = row[i]
        if len(col) == 0: continue
        
        s = sorted(col.items())
        for j in range(1, len(s)):
            y1, node1 = s[j - 1]
            y2, node2 = s[j]

            node1.r = node2
            node2.l = node1
        
        cur = s[0][1]
    
    ans = 0
    for x, y in ops:
        cur = nodes[(x, y)]
        if cur.end: continue
        cur_ = cur.r
        while cur_:
            if cur_.flag == MIRROR:
                break
            cur_.end = True
            ans += 1

            if cur_.l:
                cur_.l.r = cur_.r
            
            if cur_.r:
                cur_.r.l = cur_.l

            cur_ = cur_.r
        
        cur_ = cur.l
        while cur_:
            if cur_.flag == MIRROR:
                break

            cur_.end = True
            ans += 1

            if cur_.l:
                cur_.l.r = cur_.r
            
            if cur_.r:
                cur_.r.l = cur_.l

            cur_ = cur_.l
    
    print(n - ans)