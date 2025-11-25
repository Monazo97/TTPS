#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)

int main() {
    FIN;

    int n; cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++) {
        cin >> v[i];
    }
    int ans = 1;
    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            ans = max(ans, __gcd(v[i], v[j]));
        }
    }
    cout << ans << "\n";
    return 0;
}