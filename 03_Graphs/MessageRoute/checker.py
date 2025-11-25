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

firstLine = ouf.readline().strip()
firstLineAns = ans.readline().strip()
if firstLine == firstLineAns == "IMPOSSIBLE":
    print("Accepted")
    sys.exit(0)

k = int(firstLine)
kAns = int(firstLineAns)

if k != kAns:
    print("Wrong Answer: Different minimum path")
    sys.exit(1)

path = list(map(int, ouf.readline().strip().split()))
if len(path) != k:
    print("Wrong Answer: Path length does not match k")
    sys.exit(1)

for i in range(0, k-1):
    u = path[i] - 1
    v = path[i+1] - 1
    if u < 0 or u >= n or v < 0 or v >= n:
        print("Wrong Answer: Node out of range")
        sys.exit(1)
    if v not in g[u]:
        print("Wrong Answer: Invalid path, edge does not exist")
        sys.exit(1)

# Check EOF
if ouf.readline():
    print("Wrong Answer: Extra data at the end of the file")
    sys.exit(1)

print("Accepted")
