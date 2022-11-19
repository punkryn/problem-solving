import sys
sys.setrecursionlimit(10**9)
def solution(n, lighthouse):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    for x, y in lighthouse:
        graph[x].append(y)
        graph[y].append(x)
    
    def DFS(x, prev):
        nonlocal answer
        if x != 1 and len(graph[x]) == 1:
            return True
        
        flag = False
        for nxt in graph[x]:
            if nxt == prev: continue
            
            flag |= DFS(nxt, x)
            
        if flag:
            answer += 1
            return False
        return True
    DFS(1, 0)
    
    return answer