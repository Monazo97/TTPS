#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
#define FIN ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
 
ll digits(ll n) {
	ll aux = 9, ans = 0, ind = 1;
	ll cur = 0;
	while(n > cur + aux) {
		ans += aux * ind;
		cur += aux;
		aux *= 10; ind++;
	}
	ans += ind * (n - cur);
	return ans;
}
 
int main(){
  FIN;
	int t; cin >> t;
	while(t--) {
		ll n; cin >> n;
		ll a = 0, b = (ll)(1e18);
		while(b-a > 1) {
			ll med = (a+b)/2;
			ll cont = digits(med);
			if(cont >= n) b = med;
			else a = med;
		}
		ll cont = digits(b);
		while(cont > n) b /= 10, cont--;
		cout << b%10 << "\n";
	}
	
	return 0;
}
