# https://www.acmicpc.net/problem/14719
import sys
si = sys.stdin.readline

if __name__ == '__main__':
    h, w = map(int, si().split())
    heights = list(map(int, si().split()))
    ans = 0
    
    MAP = [[0] * w for _ in range(h)]
    mh = [0] * w
    m = -1
    for i in range(w - 1, -1, -1):
        if m < heights[i]:
            m = heights[i]
        mh[i] = m

    s = heights[0]
    for i in range(1, w - 1):
        g = min(mh[i], s) - heights[i]
        if g > 0:
            ans += g
        s = max(s, heights[i])
    
    # for i in range(w):
    #     for j in range(h - 1, h - heights[i] - 1, -1):
    #         MAP[j][i] = 1
    
    # for i in range(h - 1, -1, -1):
    #     tmp = MAP[i][:]
    #     for j in range(1, w - 1):
    #         flag = False
    #         if tmp[j] == 0:
    #             if tmp[j - 1] == 1 or tmp[j - 1] == 2:
    #                 k = j
    #                 while k + 1 < w:
    #                     k += 1
    #                     if tmp[k] == 1:
    #                         flag = True
    #                         break
    #         if flag:
    #             tmp[j] = 2
    #             ans += 1
            
    #     MAP[i] = tmp

    print(ans)