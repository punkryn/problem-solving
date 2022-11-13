# https://www.acmicpc.net/problem/5430
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    for _ in range(int(si())):
        p = si().strip()
        n = int(si())
        arr = si().strip()[1:-1]
        if not arr:
            arr = deque()
        else:
            arr = deque(map(int, arr.split(',')))
        
        flag = 1
        try:
            for op in p:
                if op == 'R':
                    flag *= -1
                else:
                    if flag == 1:
                        arr.popleft()
                    else:
                        arr.pop()
            if flag == 1:
                print(f'[{",".join(map(str, arr))}]')
            else:
                arr.reverse()
                print(f'[{",".join(map(str, arr))}]')
        except:
            print('error')