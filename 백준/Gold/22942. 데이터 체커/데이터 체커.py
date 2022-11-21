# https://www.acmicpc.net/problem/22942
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

LEFT=0
RIGHT=1

if __name__ == '__main__':
    n = int(si())
    a = []

    for i in range(n):
        x, r = mis()
        a.append((x - r, LEFT, i))
        a.append((x + r, RIGHT, i))
    
    a.sort()

    st = []
    ans = True
    for pos, t, idx in a:
        if not st:
            if t == RIGHT:
                ans = False
                break
            st.append((pos, t, idx))
        else:
            if t == RIGHT:
                top = st.pop()
                if top[1] != LEFT or top[2] != idx:
                    ans = False
                    break
            else:
                st.append((pos, t, idx))
    
    if st: ans = False
    
    print('YES' if ans else 'NO')