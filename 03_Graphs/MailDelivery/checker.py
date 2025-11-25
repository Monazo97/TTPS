import sys
# Extend recursion limit for deep DFS
sys.setrecursionlimit(10**7)

_input, _output, _ans = sys.argv[1], sys.argv[2], sys.argv[3]
inf = open(_input, "r")
ouf = open(_output, "r")
ans = open(_ans, "r")

edges = set()

n,m = map(int, inf.readline().strip().split())
g = [[] for _ in range(n)]
for i in range(m):
    u,v = map(int, inf.readline().strip().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    edges.add((min(u,v), max(u,v)))

firstLine = ouf.readline().strip()
firstLineAns = ans.readline().strip()

if firstLine == firstLineAns == "IMPOSSIBLE":
    print("Accepted")
    sys.exit(0)

eulerPath = list(map(int, firstLine.split()))

if len(eulerPath) != m + 1:
    print("Wrong Answer: Eulerian path length incorrect")
    sys.exit(1)

for i in range(1,m+1):
    x = eulerPath[i-1] - 1
    y = eulerPath[i] - 1
    if x < 0 or x >= n or y < 0 or y >= n:
        print("Wrong Answer: Node out of range")
        sys.exit(1)
    if (min(x,y), max(x,y)) not in edges:
        print("Wrong Answer: Edge does not exist")
        sys.exit(1)
    edges.remove((min(x,y), max(x,y)))
    
# Check EOF
if ouf.readline():
    print("Wrong Answer: Extra data at the end of the file")
    sys.exit(1)

print("Accepted")
