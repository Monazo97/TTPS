import sys
# Extend recursion limit for deep DFS
sys.setrecursionlimit(10**7)

_input, _output, _ans = sys.argv[1], sys.argv[2], sys.argv[3]
inf = open(_input, "r")
ouf = open(_output, "r")
ans = open(_ans, "r")

n,m = map(int, inf.readline().strip().split())
g = [[] for _ in range(n)]
for i in range(m):
    u,v = map(int, inf.readline().strip().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

k = int(ouf.readline().strip())
kAns = int(ans.readline().strip())

if k != kAns:
    print("Wrong Answer: Different number of components")
    sys.exit(1)

for i in range(k):
    try:
        u,v = map(int, ouf.readline().strip().split())
    except ValueError:
        print("Wrong Answer: Invalid input format")
        sys.exit(1)
    u -= 1
    v -= 1
    if u < 0 or u >= n or v < 0 or v >= n:
        print("Wrong Answer: Node out of range")
        sys.exit(1)
    if u == v:
        print("Wrong Answer: Component of size 1")
        sys.exit(1)
    g[u].append(v)
    g[v].append(u)

# Check EOF
if ouf.readline():
    print("Wrong Answer: Extra data at the end of the file")
    sys.exit(1)

visited = [False]*n

def dfs(u):
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs(v)

dfs(0)
if not all(visited):
    print("Wrong Answer: Graph is not connected")
    sys.exit(1)

print("Accepted")
