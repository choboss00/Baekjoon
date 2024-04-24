N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

ans = 0
def dfs(x, y):
    global ans
    # 방문 처리
    visited[y][x] = True
    cycle.append([x, y])

    if board[y][x] == 'U':
        y -= 1
    elif board[y][x] == 'L':
        x -= 1
    elif board[y][x] == 'R':
        x += 1
    elif board[y][x] == 'D':
        y += 1

    if visited[y][x]:
        if [x, y] in cycle:
            ans += 1
    else:
        dfs(x, y)

for y in range(N):
    for x in range(M):
        if not visited[y][x]:
            cycle = []
            dfs(x, y)

print(ans)
