MAXVAL = 100005
import sys

n = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))

dp = [0] * MAXVAL

for u in v:
    j = 1
    while j * j <= u:
        if u % j == 0:
            aux1 = max(dp[u], dp[j] + 1)
            aux2 = max(dp[u], dp[u // j] + 1)
            dp[u] = max(aux1, aux2)
        j += 1
    dp[u] = max(dp[u], 1)

print(max(dp))
