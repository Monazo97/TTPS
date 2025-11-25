import sys

MAXVAL = 10**6 + 1
n = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))

cont = [0] * MAXVAL

for x in v:
    for div in range(1, int(x**0.5) + 1):
        if x % div == 0:
            cont[div] += 1
            if div * div != x:
                cont[x // div] += 1

ans = 1
for i in range(1, MAXVAL):
    if cont[i] >= 2:
        ans = i

sys.stdout.write(str(ans) + "\n")