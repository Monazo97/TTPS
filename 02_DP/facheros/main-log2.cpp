#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define FIN ios::sync_with_stdio(0);cout.tie(0);cin.tie(0)
#define all(c) (c).begin(),(c).end()
#define DBG(ans) for(int i = 0; i < 5; i++) {for(int j = 0; j < 5; j++) cerr << ans[i][j] << " "; cerr << endl;}
#define forr(i,a,b) for(int i = int(a); i < int(b); i++)
#define forn(i,n) forr(i,0,n)
const ll MOD = 1e9+7;

typedef vector<vector<ll>> Matrix;

Matrix ones(int n) {
    Matrix r(n,vector<ll>(n));
    forn(i,n)r[i][i]=1;
    return r;
}
Matrix operator*(Matrix &a, Matrix &b) {
    int n=a.size(),m=b[0].size(),z=a[0].size();
    Matrix r(n,vector<ll>(m));
    forn(i,n)forn(j,m)forn(k,z)
        r[i][j]+=a[i][k]*b[k][j],r[i][j]%=MOD;
    return r;
}
Matrix be(Matrix b, ll e) {
    Matrix r=ones(b.size());
    while(e){if(e&1LL)r=r*b;b=b*b;e/=2;}
    return r;
}

int main() {
	FIN;
	
	ll n; cin >> n;
	vector<vector<ll>> m = {
		{0,1,0,0,0},
		{1,0,1,0,0},
		{0,1,0,1,0},
		{0,0,1,0,1},
		{0,0,0,1,0}
	};
	vector<vector<ll>> ans = {
		{1},
		{1},
		{1},
		{1},
		{1}
	};
	
	m = be(m,n-1);
	ans = m * ans;
	ll total = 0;
	for(auto v : ans) for(ll u : v) total += u, total %= MOD;
	cout << total << "\n";
	return 0;
}
