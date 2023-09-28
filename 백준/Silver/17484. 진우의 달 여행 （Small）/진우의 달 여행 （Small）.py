import sys

# 방향
direction = [-1,0,1]
def dfs(x, y, d, num):
    if y == n-1:
        ans_list.append(num)

    for i in direction:
        if i != d:
            if 0 <= x + i < m and 0 <= y + 1 < n:
                dfs(x + i, y + 1, i, num + board[y+1][x+i])

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

ans_list = []

for i in range(m):
    dfs(i, 0, 222, board[0][i])

print(min(ans_list))