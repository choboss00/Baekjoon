import sys

input = sys.stdin.readline

n = int(input())
n_list = []
# 삼각형 채우기
for _ in range(n):
    n_list.append(list(map(int, input().split())))

dp = []

for i in range(n+1):
    zero_list = [0] * (i+1)

    dp.append(zero_list)
# 뒤집기 ( 끝부터 더하기 위해 )
n_list.reverse()
dp.reverse()

for j in range(1, n+1):
    for k in range(len(dp[j])):
        dp[j][k] = max(dp[j-1][k], dp[j-1][k+1]) + n_list[j-1][k]

print(*dp[-1])