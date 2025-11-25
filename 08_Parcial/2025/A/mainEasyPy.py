import sys

INF = int(1e18)

def main():
    n = int(input())
    v = []
    for _ in range(n):
        a, b = map(int, input().split())
        v.append((a, b))
    
    v.sort()
    ans = INF
    
    for i in range(n - 1):
        ans = min(ans, v[i + 1][0] - v[i][0])
    
    print(f"{ans:.10f}")

if __name__ == "__main__":
    main()
