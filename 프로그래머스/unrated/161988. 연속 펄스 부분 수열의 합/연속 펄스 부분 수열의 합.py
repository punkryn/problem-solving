def solution(sequence):
    answer = 0
    l = len(sequence)
    if l == 1:
        return abs(sequence[0])
    
    prev = sequence[0]
    cur = 0
    answer = prev
    for i in range(1, l):
        cur = max(sequence[i] * (1 if i % 2 == 0 else -1), prev + sequence[i] * (1 if i % 2 == 0 else -1))
        answer = max(answer, cur)
        
        prev = cur
    
    prev = sequence[0] * -1
    cur = 0
    for i in range(1, l):
        cur = max(sequence[i] * (1 if i % 2 == 1 else -1), prev + sequence[i] * (1 if i % 2 == 1 else -1))
        answer = max(answer, cur)
        
        prev = cur
    
    return answer