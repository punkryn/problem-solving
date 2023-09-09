def solution(picks, minerals):
    answer = float('inf')
    
    n = len(minerals) // 5 + (1 if len(minerals) % 5 != 0 else 0)
    arr = []
    
    cost = {
        0: {'diamond': 1, 'iron': 1, 'stone': 1},
        1: {'diamond': 5, 'iron': 1, 'stone': 1},
        2: {'diamond': 25, 'iron': 5, 'stone': 1},
    }
    
    def go(depth):
        nonlocal answer
        if depth == n or sum(picks) == 0:
            SUM = 0
            for i in range(len(arr)):
                pick = arr[i]
                for j in range(5 * i, min(5 * (i + 1), len(minerals))):
                    SUM += cost[pick][minerals[j]]
            answer = min(answer, SUM)
            return
        
        for i in range(3):
            if picks[i] == 0:
                continue
            
            picks[i] -= 1
            arr.append(i)
            go(depth + 1)
            arr.pop()
            picks[i] += 1
    
    go(0)
    
    return answer