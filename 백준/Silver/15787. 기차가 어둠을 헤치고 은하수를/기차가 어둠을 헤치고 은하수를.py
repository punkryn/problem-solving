import sys
si = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, si().split())
    trains = [0] * (n + 1)
    visited = set()
    for _ in range(m):
        oper = list(map(int, si().split()))
        if oper[0] == 1:
            idx = oper[1]
            x = oper[2]
            trains[idx] |= (1 << (x - 1))
        elif oper[0] == 2:
            idx = oper[1]
            x = oper[2]
            trains[idx] &= (~(1 << (x - 1)))
        elif oper[0] == 3:
            idx = oper[1]
            trains[idx] = (trains[idx] << 1) & ((2 ** 20) - 1)
        elif oper[0] == 4:
            idx = oper[1]
            trains[idx] = (trains[idx] >> 1)
    
    ans = 0
    for train in trains[1:]:
        if train in visited:
            continue

        visited.add(train)
        ans += 1
    print(ans)