# https://www.acmicpc.net/problem/14863
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n, k = mis()
    infos = [list(mis()) for _ in range(n)]

    dp = [[0] * (k + 1) for _ in range(n)]
    dp[0][infos[0][0]] = infos[0][1]
    dp[0][infos[0][2]] = max(dp[0][infos[0][2]], infos[0][3])

    for i in range(1, n):
        for j in range(infos[i][0], k + 1):
            prev = j - infos[i][0]
            if dp[i - 1][prev] == 0: continue
            dp[i][j] = max(dp[i][j], dp[i - 1][prev] + infos[i][1])
            
                
        for j in range(infos[i][2], k + 1):
            prev = j - infos[i][2]
            if dp[i - 1][prev] == 0: continue
            dp[i][j] = max(dp[i][j], dp[i - 1][prev] + infos[i][3])
    
    print(max(dp[n - 1]))
                