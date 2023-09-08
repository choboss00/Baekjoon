import sys

input = sys.stdin.readline

n = int(input())

ans = 0

for num in range(1, n+1):
    ans += (num * (n // num))

print(ans)