#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int main() {
    FIN;

    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        int ans = 0;
        for(int i = 1; i*i <= n; i++) {
            if(n%i == 0) ans++;
            if(i*i != n and n%i == 0) ans++; 
        }
        cout << ans << endl;
    }
}