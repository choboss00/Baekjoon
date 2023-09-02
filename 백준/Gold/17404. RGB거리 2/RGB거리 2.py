import sys

input = sys.stdin.readline

n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

E = 1e9
ans = 1e9

for i in range(3):
    dp = [[E, E, E] for _ in range(n)]
    # 첫번째 집 색칠
    dp[0][i] = board[0][i]

    for j in range(1, n):
        dp[j][0] = board[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = board[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = board[j][2] + min(dp[j - 1][1], dp[j - 1][0])

    for c in range(3):
        # 첫번째 집과 달라야 함
        if i != c:
            ans = min(ans, dp[-1][c])

print(ans)