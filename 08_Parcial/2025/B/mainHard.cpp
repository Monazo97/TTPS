#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
typedef long long ll;

const int MAXVAL = 1e5+5;

int main() {
    FIN;

    int n; cin >> n;
    vector <int> v(n), dp(MAXVAL, 0);
    for(int i = 0; i < n; i++) {
        cin >> v[i];
    }
    for(int i = 0; i < n; i++) {
        for(int j = 1; j * j <= v[i]; j++) {
            if(v[i] % j == 0) {
                int aux1 = max(dp[v[i]], dp[j] + 1);
                int aux2 = max(dp[v[i]], dp[v[i]/j] + 1);
                dp[v[i]] = max(aux1, aux2);
            }
        }
        dp[v[i]] = max(dp[v[i]], 1);
    }
    
    cout << *max_element(dp.begin(), dp.end()) << "\n";
    return 0;
}