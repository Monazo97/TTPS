#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
typedef long long ll;

const ll INF = 1e18;

typedef long long ll;

struct Edge {
	int x, y; 
	ll w;
	bool operator < (Edge aux) {
		return w < aux.w;
	}
};
 
struct DSU {
    vector<int> link, sz;
 
    DSU(int n) {
        link.resize(n);
        sz.resize(n, 1); // Tamaño de cada componente
        for (int i = 0; i < n; i++) {
            link[i] = i; // Cada nodo es su propio padre
        }
    }
 
    int getLink(int x) {
        if (link[x] != x) { // Si no es su propio padre
            link[x] = getLink(link[x]); // Path compression
        }
        return link[x];
    }
 
    void unionSets(int x, int y) {
        x = getLink(x);
        y = getLink(y);
        if (x != y) { // Si no estan en la misma componente
            if (sz[x] < sz[y]) {
                swap(x, y); // Asegurarse de que x es la componente mas grande
            }
            link[y] = x;
            sz[x] += sz[y];
        }
    }
};
 
 
ll kruskal(int n, vector<Edge> &aristas, int m) {
	DSU dsu(n);
	ll costo = 0, cont = 0;
	for(int i = 0; i < m; i++) {
		auto [x,y,w] = aristas[i];
		if(dsu.getLink(x) != dsu.getLink(y)) {
			costo = w;
			cont++;
			dsu.unionSets(x,y);
		}
	}
	if(cont != n-1) return -1;
	return costo;
}

int main() {
    FIN;
    int n;
    cin >> n;
    vector<pair<ll,ll>> v(n);
    for(int i = 0; i < n; i++) {
        cin >> v[i].first >> v[i].second;
    }
    
    vector<Edge> edges;
    for(int i = 0; i < n; i++) {
        for(int j = i+1; j < n; j++) {
            ll dist = (v[i].first - v[j].first) * (v[i].first - v[j].first) + (v[i].second - v[j].second) * (v[i].second - v[j].second);
            edges.push_back({i, j, dist});
        }
    }
    sort(edges.begin(), edges.end());

    cout << fixed << setprecision(10) << sqrtl(kruskal(n, edges, edges.size())) << "\n";

    return 0;
}