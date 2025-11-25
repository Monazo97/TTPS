import sys
import math

INF = int(1e18)

class Edge:
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
    
    def __lt__(self, other):
        return self.w < other.w

class DSU:
    def __init__(self, n):
        self.link = [0] * n # Padre de cada nodo
        self.sz = [1] * n # Tamaño de cada componente
        for i in range(n):
            self.link[i] = i # Cada nodo es su propio padre
            
    def getLink(self, x):
        if self.link[x] != x: # Si no es su propio padre
            self.link[x] = self.getLink(self.link[x]) # Path compression
        return self.link[x]
            
    def union(self, x, y):
        x = self.getLink(x)
        y = self.getLink(y)
        if x != y: # Si no estan en la misma componente
            if self.sz[x] < self.sz[y]:
                x,y = y,x # Asegurarse de que x es la componente mas grande
            self.link[y] = x
            self.sz[x] += self.sz[y]
        return self.sz[x]

def kruskal(n, aristas, m):
    dsu = DSU(n)
    costo = 0
    cont = 0
    for i in range(m):
        x, y, w = aristas[i].x, aristas[i].y, aristas[i].w
        if dsu.getLink(x) != dsu.getLink(y):
            costo = w
            cont += 1
            dsu.union(x, y)
    if cont != n - 1:
        return -1
    return costo

def main():
    n = int(sys.stdin.readline())
    v = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        v.append((a, b))
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = (v[i][0] - v[j][0]) * (v[i][0] - v[j][0]) + (v[i][1] - v[j][1]) * (v[i][1] - v[j][1])
            edges.append(Edge(i, j, dist))
    
    edges.sort()
    
    result = math.sqrt(kruskal(n, edges, len(edges)))
    print(f"{result:.10f}")

if __name__ == "__main__":
    main()
