import sys
import heapq

class Edge:
    def __init__(self, x, y, w):
        self.x = x # From
        self.y = y # To
        self.w = w # Weight

class Node:
    def __init__(self, id, d, prev):
        self.id = id
        self.d = d
        self.prev = prev
    
    def __lt__(self, other):
        return self.d < other.d

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, x, y, w):
        self.adj[x].append(Edge(x, y, w))

INF = 10**18

def dijkstra(grafo, s):
    n = grafo.n
    dist = [INF] * n
    dist[s] = 0
    pq = []
    ans = [0] * n
    heapq.heappush(pq, Node(0, 0, -1))

    while pq:
        u = heapq.heappop(pq)
        if u.d > dist[u.id]:
            continue
        ans[u.id] = u
        for edge in grafo.adj[u.id]:
            v = edge.y
            weight = edge.w
            if dist[u.id] + weight < dist[v]:
                dist[v] = dist[u.id] + weight
                heapq.heappush(pq, Node(v, dist[v], u.id))
    
    return ans

n, m = map(int, sys.stdin.readline().split())
grafo = Graph(n)

for i in range(m):
    x, y, w = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    grafo.add_edge(x, y, w)

ans = dijkstra(grafo, 0)
sys.stdout.write(' '.join([str(p.d) for p in ans]))
sys.stdout.write(' \n')