#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0);cout.tie(0);cin.tie(0)

typedef long long ll;
const int MOD = 1e9+7;

ll be(ll p, ll k, ll MOD) {
	if(k == 0) return 1LL;
	ll aux = be(p,k/2,MOD);
	aux *= aux; aux %= MOD;
	if(k&1) aux *= p; aux %= MOD;
	return aux;
}

int main() {
	FIN;
	
	int k; cin >> k;
	if(k == 1) {
		cout << "5\n";
		return 0;
	}
	if(k == 2) {
		cout << "8\n";
		return 0;
	}
	if(k == 3) {
		cout << "14\n";
		return 0;
	}
	ll ans;
	if(k%2 == 0) {
		k -= 2;
		k /= 2;
		ans = 8;
		ans *= be(3,k,MOD);
	} else {
		k -= 3;
		k /= 2;
		ans = 14;
		ans *= be(3,k,MOD);
	}
	ans %= MOD;
	cout << ans << "\n";
	
	return 0;	
}
