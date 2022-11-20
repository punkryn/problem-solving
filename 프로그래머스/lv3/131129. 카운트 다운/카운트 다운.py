INF = int(10**9)
def solution(target):
    answer = []
    
    dp = [[INF, 0] for _ in range(target + 1)]
    dp[0][0] = 0
    for i in range(target):
        for j in range(1, 21):
            nxt = dp[i][0] + 1
            nxtIdx = i + j
            if nxtIdx <= target :
                if nxt < dp[nxtIdx][0]:
                    dp[nxtIdx][0] = nxt
                    dp[nxtIdx][1] = dp[i][1] + 1
                elif nxt == dp[nxtIdx][0]:
                    dp[nxtIdx][1] = max(dp[nxtIdx][1], dp[i][1] + 1)
            
            nxtIdx = i + j * 2
            if nxtIdx <= target:
                if nxt < dp[nxtIdx][0]:
                    dp[nxtIdx][0] = nxt
                    dp[nxtIdx][1] = dp[i][1]
                elif nxt == dp[nxtIdx][0]:
                    dp[nxtIdx][1] = max(dp[nxtIdx][1], dp[i][1])
            
            nxtIdx = i + j * 3
            if nxtIdx <= target:
                if nxt < dp[nxtIdx][0]:
                    dp[nxtIdx][0] = nxt
                    dp[nxtIdx][1] = dp[i][1]
                elif nxt == dp[nxtIdx][0]:
                    dp[nxtIdx][1] = max(dp[nxtIdx][1], dp[i][1])
        
        nxtIdx = i + 50
        if nxtIdx <= target:
            if nxt < dp[nxtIdx][0]:
                dp[nxtIdx][0] = nxt
                dp[nxtIdx][1] = dp[i][1] + 1
            elif nxt == dp[nxtIdx][0]:
                dp[nxtIdx][1] = max(dp[nxtIdx][1], dp[i][1] + 1)
        
    return dp[target]