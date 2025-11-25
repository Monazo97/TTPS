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

k = int(firstLine)
kAns = int(firstLineAns)

if k != kAns:
    print("Wrong Answer: Different necessary roads")
    sys.exit(1)

roads = set()

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
        print("Wrong Answer: Road to self")
        sys.exit(1)
    roads.add((min(u,v), max(u,v)))

ansRoads = set()

for i in range(k):
    try:
        u,v = map(int, ans.readline().strip().split())
    except ValueError:
        print("Wrong Answer: Invalid input format")
        sys.exit(1)
    u -= 1
    v -= 1
    if u < 0 or u >= n or v < 0 or v >= n:
        print("Wrong Answer: Node out of range")
        sys.exit(1)
    if u == v:
        print("Wrong Answer: Road to self")
        sys.exit(1)
    ansRoads.add((min(u,v), max(u,v)))

# Check EOF
if ouf.readline():
    print("Wrong Answer: Extra data at the end of the file")
    sys.exit(1)

if roads != ansRoads:
    print("Wrong Answer: Different necessary roads")
    sys.exit(1)

print("Accepted")
