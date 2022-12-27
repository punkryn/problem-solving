# https://www.acmicpc.net/problem/1036
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    z = dict()
    zz = dict()
    cnt = dict()
    score = dict()
    for w in range(10):
        z[w] = str(w)
        zz[str(w)] = w
        cnt[str(w)] = 0
        score[str(w)] = 0
    
    for w in range(ord('A'), ord('Z') + 1):
        z[w - ord('A') + 10] = chr(w)
        zz[chr(w)] = w - ord('A') + 10
        cnt[chr(w)] = 0
        score[chr(w)] = 0
    
    words = []
    for _ in range(n):
        word = si().strip()
        words.append(list(word))
        for i in range(len(word)):
            score[word[i]] += zz[word[i]] * (36 ** (len(word) - i - 1))
            cnt[word[i]] += zz['Z'] * (36 ** (len(word) - i - 1))
    
    k = int(si())
    
    cand = set(sorted(cnt.keys(), key=lambda x: (cnt[x] - score[x], -ord(x)), reverse=True)[:k])
    
    ans = 0
    for word in words:
        for i in range(len(word)):
            if word[i] in cand:
                ans += zz['Z'] * (36 ** (len(word) - i - 1))
                continue
            ans += zz[word[i]] * (36 ** (len(word) - i - 1))

    if ans == 0:
        print(0)
        exit()

    answer = []
    while ans:
        answer.append(z[ans % 36])
        ans //= 36
    print(''.join(answer[::-1]))