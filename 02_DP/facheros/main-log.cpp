#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define FIN ios::sync_with_stdio(0);cout.tie(0);cin.tie(0)
#define all(c) (c).begin(),(c).end()
#define DBG(ans) for(int i = 0; i < 5; i++) {for(int j = 0; j < 5; j++) cerr << ans[i][j] << " "; cerr << endl;}
const ll MOD = 1e9+7;

vector<vector<ll>> ones = {
							{1,0,0,0,0},
							{0,1,0,0,0},
							{0,0,1,0,0},
							{0,0,0,1,0},
							{0,0,0,0,1},
						};

vector<vector<ll>> merge(vector<vector<ll>> a, vector<vector<ll>> b) {
	vector<vector<ll>> ans(5,vector<ll>(5));
	for(int x1 = 0; x1 < 5; x1++) {
		for(int y1 = 0; y1 < 5; y1++) {
			for(int x2 = 0; x2 < 5; x2++) {
				for(int y2 = 0; y2 < 5; y2++) {
					if(abs(y1-x2) != 1) continue;
					ans[x1][y2] += a[x1][y1] * b[x2][y2];
					ans[x1][y2] %= MOD;
				}
			}
		}
	}
	return ans;
}

vector <vector<ll>> solve(ll n) {
	if(n == 1) {
		return ones;
	}
	vector <vector<ll>> ans = solve(n/2);
	ans = merge(ans,ans);
	if(n%2 == 1) ans = merge(ans,ones);
	return ans;
}

int main() {
	FIN;
	
	ll n; cin >> n;
	vector<vector<ll>> ans = solve(n);
	ll total = 0;
	for(int i = 0; i < 5; i++) {
		for(int j = 0; j < 5; j++) {
			//~ cerr << ans[i][j] << " ";
			total += ans[i][j];
			total %= MOD;
		}
		//~ cerr << endl;
	}
	cout << total << "\n";
	
	
	//~ cout << accumulate(all(ans),0LL) % MOD;
	
	
	return 0;
}
