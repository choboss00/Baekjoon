import sys

ans = 0
def dfs(x,y,d):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return
    else:
        if d == 0 or d == 2:
            dx = x + 1
            # 그 다음위치를 갈 수 있는 경우
            if dx < n and board[y][dx] == 0:
                dfs(dx, y, 0)
        if d == 1 or d == 2:
            dy = y + 1
            if dy < n and board[dy][x] == 0:
                dfs(x, dy, 1)

        dx = x + 1
        dy = y + 1
        if dx < n and dy < n:
            if board[dy-1][dx] == 0 and board[dy][dx-1] == 0 and board[dy][dx] == 0:
                dfs(dx,dy,2)


input = sys.stdin.readline

n = int(input())
board = []
# map 만들기
for _ in range(n):
    board.append(list(map(int, input().split())))

if (board[0][2] == 1 and board[1][1] == 1) or (board[n-1][n-2] == 1 and board[n-2][n-1] == 1) or board[n-1][n-1] == 1:
    print(0)
else:
    dfs(1,0,0)
    print(ans)