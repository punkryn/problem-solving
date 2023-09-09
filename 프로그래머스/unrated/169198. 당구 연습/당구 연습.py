def solution(m, n, startX, startY, balls):
    answer = []
    
    for x, y in balls:
        dist = float('inf')
        # 꼭짓점
        # 좌상
        if startX < x and startY > y and startX * (n - y) == (n - startY) * x:
            dist = min(dist, (startX + x) ** 2 + (n - startY + n - y) ** 2)
        # 우상
        if startX > x and startY > y and (m - startX) * (n - y) == (n - startY) * (m - x):
            dist = min(dist, (m - startX + m - x) ** 2 + (n - startY + n - y) ** 2)
        # 좌하
        if  startX < x and startY < y and startX * y == startY * x:
            dist = min(dist, (startX + x) ** 2 + (startY + y) ** 2)
        # 우하
        if startX > x and startY < y and (m - x) * startY == (m - startX) * y:
            dist = min(dist, (m - startX + m - x) ** 2 + (startY + y) ** 2)
            
        # 모서리
        # 위
        if not (x == startX and startY < y):
            dist = min(dist, (x - startX) ** 2 + (n - y + n - startY) ** 2)
        # 아래
        if not (x == startX and startY > y):
            dist = min(dist, (x - startX) ** 2 + (y + startY) ** 2)
        # 좌
        if not (y == startY and x < startX):
            dist = min(dist, (x + startX) ** 2 + (y - startY) ** 2)
        # 우
        if not (y == startY and x > startX):
            dist = min(dist, (m - x + m - startX) ** 2 + (y - startY) ** 2)
        
        answer.append(dist)
    
    return answer