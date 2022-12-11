# https://www.acmicpc.net/problem/26155
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == '__main__':
    n, m = mis()
    infos = []
    for _ in range(m):
        a, b, p = si().split()
        a = int(a)
        b = int(b)
        p = float(p)
        infos.append((a, b, p))
    
    infos.sort(key=lambda x: x[2], reverse=True)

    q = int(si())
    query = []
    for i in range(q):
        query.append((float(si()), i))
    
    query.sort(reverse=True)
    
    parent = [i for i in range(n + 1)]
    
    ans = [0] * q
    idx = 0

    cnt = n
    for i in range(q):
        while idx < m and query[i][0] <= infos[idx][2]:
            if find_parent(infos[idx][0]) != find_parent(infos[idx][1]):
                union(infos[idx][0], infos[idx][1])
                cnt -= 1

            idx += 1
        
        if len(query[i]) != 2 or query[i][1] >= q: break
        ans[query[i][1]] = cnt
    
    for i in range(len(ans)):
        print(ans[i])