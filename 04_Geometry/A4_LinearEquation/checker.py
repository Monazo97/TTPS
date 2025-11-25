import sys
# Extend recursion limit for deep DFS
sys.setrecursionlimit(10**7)

EPS = 1e-6

_input, _output, _ans = sys.argv[1], sys.argv[2], sys.argv[3]
inf = open(_input, "r")
ouf = open(_output, "r")
ans = open(_ans, "r")

t = int(inf.readline().strip())

oufLines = ouf.readlines()
ansLines = ans.readlines()

if len(oufLines) < t:
    sys.stdout.write(f"Output file has less lines ({len(oufLines)}) than test cases ({t}).\n")
    sys.exit(1)

for i in range(t):
    oufLine = oufLines[i].strip()
    ansLine = ansLines[i].strip()
    if ansLine == 'SAME' and oufLine == ansLine:
        continue
    if ansLine == 'PARALLEL' and oufLine == ansLine:
        continue
    pointAns = list(map(float, ansLine.split()))
    pointOuf = list(map(float, oufLine.split()))
    # Check that pointOuf is a list of two floats
    if len(pointOuf) != 2:
        sys.stdout.write(f"Test case {i+1}: Output point does not have two coordinates.\n")
        sys.exit(1)
    
    errorX = abs(pointAns[0] - pointOuf[0])
    errorY = abs(pointAns[1] - pointOuf[1])
    if errorX > EPS or errorY > EPS:
        sys.stdout.write(f"Test case {i+1}: Point differs from expected answer by more than {EPS}.\n")
        sys.exit(1)

sys.stdout.write("All test cases passed!\n")
sys.exit(0)
