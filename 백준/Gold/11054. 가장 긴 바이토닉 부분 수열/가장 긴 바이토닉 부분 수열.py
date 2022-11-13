# https://www.acmicpc.net/problem/11054
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    a = list(mis())

    dp = [[1] * 2 for _ in range(n + 1)]
    
    ans = 1
    for i in range(1, n):
        for j in range(i):
            # up
            if a[i] > a[j]:
                dp[i][0] = max(dp[i][0], dp[j][0] + 1)
            
            # down
            if a[i] < a[j]:
                dp[i][1] = max(dp[i][1], dp[j][1] + 1, dp[j][0] + 1)
            
            ans = max(ans, dp[i][0], dp[i][1])
    
    print(ans)