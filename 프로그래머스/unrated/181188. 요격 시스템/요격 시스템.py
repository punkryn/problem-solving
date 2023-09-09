def solution(targets):
    answer = 0
    r = 0
    
    for s, e in sorted(targets):
        if r <= s:
            answer += 1
            r = e
            continue
        
        r = min(r, e)
    
    
    return answer