#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
const int MOD = 1e9 + 7;

vector<vector<int>> binCoef(int n) {
    vector<vector<int>> c(n + 1, vector<int>(n + 1, 0));
    for(int i = 0; i <= n; i++) {
        c[i][0] = 1;
        for(int j = 1; j <= i; j++) {
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
            if(c[i][j] > MOD) c[i][j] -= MOD;
        }
    }
    return c;
}

int main() {
    FIN;

    vector<vector<int>> c = binCoef(1000);
    int t; cin >> t;
    while(t--) {
        int n, m;
        cin >> n >> m;
        cout << c[n][m] << "\n";
    }
}