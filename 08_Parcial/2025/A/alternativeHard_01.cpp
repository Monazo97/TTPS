#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
typedef long long ll;

const ll INF = 1e18;

typedef long long ll;
typedef long double ld;

ld dist(pair<ll,ll> &a, pair<ll,ll> &b) {
    return sqrtl((a.first - b.first) * (a.first - b.first) + (a.second - b.second) * (a.second - b.second));
}

void DFS(int u, ld mid, vector<bool> &visited, vector<pair<ll,ll>> &v) {
    visited[u] = true;
    int n = v.size();
    for(int i = 0; i < n; i++) {
        if(!visited[i] && dist(v[u], v[i]) <= mid) {
            DFS(i, mid, visited, v);
        }
    }
}

int main() {
    FIN;
    int n;
    cin >> n;
    vector<pair<ll,ll>> v(n);
    for(int i = 0; i < n; i++) {
        cin >> v[i].first >> v[i].second;
    }
    
    ld l = 0, r = 1e7;
    for(int it = 0; it < 100; it++) {
        ld mid = (l + r) / 2.0;
        vector<bool> visited(n, false);
        DFS(0, mid, visited, v);
        bool allVisited = true;
        for(int i = 0; i < n; i++) {
            allVisited &= visited[i];
        }
        if(allVisited) {
            r = mid;
        } else {
            l = mid;
        }
    }

    cout << fixed << setprecision(10) << r << "\n";

    return 0;
}