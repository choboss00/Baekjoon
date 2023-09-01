import sys

input = sys.stdin.readline

n = int(input())

n_list = []
# 집 비용 넣기
for _ in range(n):
    n_list.append(list(map(int, input().split())))

# 최소 비용을 저장하는 리스트
dp = [[0] * 3 for _ in range(n+1)]

for i in range(1, n+1):
    # 이전까지 더했던 최솟값 + 그 다음 값
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + n_list[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + n_list[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + n_list[i-1][2]

print(min(dp[-1]))