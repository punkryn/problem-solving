# https://www.acmicpc.net/problem/15823
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

def deter(mid):
    cand = set()
    l = r = 0
    cnt = 0
    flag = True
    while l < n:
        while r < n and len(cand) < mid:
            if cards[r] in cand:
                break
            cand.add(cards[r])

            r += 1

            if len(cand) == mid:
                cnt += 1
                l += mid
                cand = set()
                flag = True
                break
        
        if flag:
            flag = False
            continue
        
        cand.remove(cards[l])
        l += 1
    return cnt >= m

if __name__ == '__main__':
    n, m = mis()
    cards = list(mis())
    
    r = len(set(cards))
    l = 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        
        if deter(mid):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    print(ans)