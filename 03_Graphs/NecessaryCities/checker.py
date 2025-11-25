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

cities = set()
citiesList = list(map(int, ouf.readline().strip().split()))

if len(citiesList) != k:
    print("Wrong Answer: Number of cities does not match k")
    sys.exit(1)

# Check EOF
if ouf.readline():
    print("Wrong Answer: Extra data at the end of the file")
    sys.exit(1)

cities = set(c-1 for c in citiesList)
    
ansCities = set()
ansCitiesList = list(map(int, ans.readline().strip().split()))

ansCities = set(c-1 for c in ansCitiesList)

if cities != ansCities:
    print("Wrong Answer: Different cities")
    sys.exit(1)

print("Accepted")
