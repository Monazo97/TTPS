#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0);cout.tie(0);cin.tie(0)

const int MOD = 1e9+7;

int main() {
	FIN;
	
	int k; cin >> k;
	vector <vector<int>> dp(k+1,vector<int>(5));
	for(int i = 0; i < 5; i++) dp[1][i] = 1;
	for(int i = 2; i <= k; i++) {
		for(int j = 0; j < 5; j++) {
			if(j-1 >= 0) dp[i][j] += dp[i-1][j-1], dp[i][j] %= MOD;
			if(j+1 < 5) dp[i][j] += dp[i-1][j+1], dp[i][j] %= MOD;
		}
	}
	int ans = 0;
	for(int u : dp[k]) ans += u, ans %= MOD;
	cout << ans << "\n";
	
	return 0;	
}
