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
