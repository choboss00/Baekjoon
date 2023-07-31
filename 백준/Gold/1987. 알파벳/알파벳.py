import sys
def bfs(x,y, alpha):
    global ans

    stack = [(x,y,alpha)]
    # 방문 처리
    visited[y][x] = board[y][x]

    while stack:
        x,y,alpha = stack.pop()
        # 최대 길이
        if ans < len(alpha):
            ans = len(alpha)

        # 끝값
        if ans == 26:
            return

        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < c and 0 <= ny < r:
                if board[ny][nx] not in alpha:
                    check = alpha + board[ny][nx]
                    # 아직 가지 않았을 경우
                    if visited[ny][nx] != check:
                        # 방문 처리
                        visited[ny][nx] = check
                        stack.append((nx,ny,check))

input = sys.stdin.readline

r,c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[[''] for _ in range(c)] for _ in range(r)]

ans = 0

bfs(0,0,board[0][0])
print(ans)