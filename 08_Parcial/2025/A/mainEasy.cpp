#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
typedef long long ll;

const ll INF = 1e18;

int main() {
    FIN;
    int n;
    cin >> n;
    vector<pair<ll,ll>> v(n);
    for(int i = 0; i < n; i++) {
        cin >> v[i].first >> v[i].second;
    }
    sort(v.begin(), v.end());
    ll ans = INF;

    for(int i = 0; i < n-1; i++) {
        ans = min(ans, v[i+1].first - v[i].first);
    }

    cout << fixed << setprecision(10) << ans << "\n";
    return 0;
}