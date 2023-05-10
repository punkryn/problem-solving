def solution(scores):
    answer = 1
    n = len(scores)
    
    m1 = [0] * 100_001
    for i in range(n):
        a, b = scores[i]
        m1[a] = max(m1[a], b)
    
    for i in range(100_000 - 1, -1, -1):
        m1[i] = max(m1[i], m1[i + 1])
    
    for i in range(n):
        a, b = scores[i]
        if a + 1 <= 100_000 and m1[a + 1] > b:
            if i == 0: return -1
            scores[i].append(-1)
            continue
        
        scores[i].append(i)
    
    scores = sorted(scores, key=lambda x: (x[0] + x[1]), reverse=True)
    sub = 1
    
    if scores[0][2] == 0:
        return 1
    
    for i in range(1, n):
        if scores[i][2] == -1:
            continue
        if sum(scores[i - 1][:2]) == sum(scores[i][:2]):
            sub += 1
        else:
            answer += sub
            sub = 1
            flag = False
        if scores[i][2] == 0:
            break
    
    return answer