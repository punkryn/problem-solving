#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <set>
#include <queue>

#define MAXN 2001
#define MAXM 2001
#define MAXGROUP 2000001

using namespace std;

int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };

int n, m, groupCnt, islandCnt, ansTime, ansCnt;
int MAP[MAXN][MAXN];

int v[MAXN][MAXM];
int island[MAXN][MAXM];
int parent[MAXGROUP];

queue<pair<int, int>> q;
queue<pair<int, int>> p;

bool oob(int x, int y) {
    return !(0 <= x && x < n && 0 <= y && y < m);
}

int find_parent(int x) {
    if (parent[x] == -1) {
        return x;
    }
    return parent[x] = find_parent(parent[x]);
}

void union_(int x, int y) {
    x = find_parent(x);
    y = find_parent(y);

    if (x < y) {
        parent[y] = x;
    }
    else {
        parent[x] = y;
    }
}

void bfs(int x, int y, int number) {
    queue<pair<int, int>> queue;
    queue.push(make_pair(x, y));
    q.push(make_pair(x, y));
    v[x][y] = number;

    while (!queue.empty()) {
        auto top = queue.front();
        queue.pop();
        x = top.first;
        y = top.second;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (oob(nx, ny))
                continue;
            if (v[nx][ny] || MAP[nx][ny] == 1 || MAP[nx][ny] == 2)
                continue;
            v[nx][ny] = number;
            queue.push(make_pair(nx, ny));
            q.push(make_pair(nx, ny));
        }
    }
}

void findIsland(int x, int y) {
    queue<pair<int, int>> islandQ;
    islandQ.push(make_pair(x, y));
    island[x][y] = 1;

    while (!islandQ.empty()) {
        int x, y;
        auto top = islandQ.front();
        islandQ.pop();
        x = top.first;
        y = top.second;

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (oob(nx, ny))
                continue;
            if (MAP[nx][ny] == 2 || island[nx][ny])
                continue;

            island[nx][ny] = 1;
            islandQ.push(make_pair(nx, ny));
        }
    }
}

bool isConnected() {
    set<int> cand;
    for (int i = 1; i <= groupCnt; i++) {
        cand.insert(find_parent(i));
    }
    return cand.size() == islandCnt;
}

bool solution() {
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        p.push(make_pair(x, y));

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (oob(nx, ny))
                continue;
            if (!v[nx][ny] || v[nx][ny] == v[x][y]) continue;
            int cur = v[x][y];
            int nxt = v[nx][ny];
            if (find_parent(cur) == find_parent(nxt)) continue;
            union_(cur, nxt);
        }
    }

    if (isConnected()) return false;

    while (!p.empty()) {
        int x = p.front().first;
        int y = p.front().second;
        p.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (oob(nx, ny)) continue;
            if (MAP[nx][ny] == 1 && !v[nx][ny]) {
                v[nx][ny] = v[x][y];
                q.push(make_pair(nx, ny));
            }
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < m; j++) {
            MAP[i][j] = tmp[j] - '0';
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (v[i][j]) continue;
            if (MAP[i][j] == 1 || MAP[i][j] == 2) continue;

            groupCnt++;
            bfs(i, j, groupCnt);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (MAP[i][j] != 0 || island[i][j])
                continue;
            islandCnt++;
            findIsland(i, j);
        }
    }

    for (int i = 0; i <= groupCnt; i++) {
        parent[i] = -1;
    }

    if (!groupCnt) {
        cout << 0 << ' ' << 0;
        return 0;
    }

    while (true) {
        if (!solution()) break;
        ansTime++;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if(v[i][j] > 0)
                ansCnt += 1;
        }
    }

    cout << ansTime << ' ' << ansCnt;
    return 0;
}