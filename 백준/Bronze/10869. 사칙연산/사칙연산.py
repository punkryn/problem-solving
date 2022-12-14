import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

if __name__ == '__main__':
    a, b = mis()
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)