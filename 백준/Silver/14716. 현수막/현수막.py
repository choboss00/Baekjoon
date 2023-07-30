import sys
sys.setrecursionlimit(10**6)
# 상 하 좌 우 대각선
D = ((0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1))
def dfs(x1,y1):
    # 현재 위치 방문 처리
    board[y1][x1] = '#'

    for i in D:
        dx = x1 + i[0]
        dy = y1 + i[1]

        if 0 <= dx < m and 0 <= dy < n:
            # 글자
            if board[dy][dx] == 1:
                dfs(dx,dy)

input = sys.stdin.readline

n,m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

# 갯수
cnt = 0

for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
            dfs(x,y)
            cnt += 1

print(cnt)