#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0);cout.tie(0);cin.tie(0);
#define SZ(x) int(x.size())
#define all(c) (c).begin(),(c).end()
#define pb push_back


// strict = 1: estrictamente creciente
int lis(vector<int> &a, int strict = 0){
	vector<int> temp; temp.pb(a[0]);
	for(int i = 1; i < a.size(); i++){
		int x = a[i];
		if(x >= temp.back()+strict) temp.pb(x);
		else {
			auto it = upper_bound(all(temp), x-strict);
			*it = x;
		}
	}
	return SZ(temp);
}

int main() {
	FIN;
	
	int n; cin >> n;
	vector <int> v(n);
	vector<int> dp(n,1);
	for(int i = 0; i < n; i++) cin >> v[i];
	cout << lis(v,1) << "\n";
	
	return 0;
}
