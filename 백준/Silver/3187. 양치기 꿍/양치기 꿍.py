import sys
sys.setrecursionlimit(10**6)
D = [(1,0), (-1,0), (0,1), (0,-1)]
v1,k1 = 0,0
def dfs(x1, y1):
    global v1
    global k1
    # 늑대일 경우
    if board[y1][x1] == 'v':
        v1 += 1

    elif board[y1][x1] == 'k':
        k1 += 1

    # 방문 처리
    board[y1][x1] = '@'

    for i in D:
        dx = x1 + i[0]
        dy = y1 + i[1]

        # 예외 처리
        if 0 <= dx < c and 0 <= dy < r:
            # 갈 수 있는 경우
            if board[dy][dx] != '#' and board[dy][dx] != '@':
                dfs(dx,dy)


input = sys.stdin.readline

r,c = map(int, input().split())

board = []
ans = [0,0]
# 지도 만들기
for _ in range(r):
    s = input().strip()
    s_list = []
    for i in s:
        s_list.append(i)
    board.append(s_list)

for y in range(r):
    for x in range(c):
        # 벽이 아닐 경우
        if board[y][x] != '#':
            dfs(x,y)
            # 늑대가 더 많았을 때
            if v1 >= k1:
                ans[1] += v1
            else:
                ans[0] += k1
            v1, k1 = 0,0
print(*ans)