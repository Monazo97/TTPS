import sys
import math

# sys.setrecursionlimit(10**6)

INF = int(1e18)

def dist(a, b):
    return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))

def DFS(u, mid, visited, v):
    visited[u] = True
    n = len(v)
    for i in range(n):
        if not visited[i] and dist(v[u], v[i]) <= mid:
            DFS(i, mid, visited, v)

def main():
    n = int(input())
    v = []
    for _ in range(n):
        a, b = map(int, input().split())
        v.append((a, b))
    
    l = 0.0
    r = 1e7
    for it in range(100):
        mid = (l + r) / 2.0
        visited = [False] * n
        DFS(0, mid, visited, v)
        allVisited = True
        for i in range(n):
            allVisited = allVisited and visited[i]
        if allVisited:
            r = mid
        else:
            l = mid
    
    print(f"{r:.10f}")

if __name__ == "__main__":
    main()
