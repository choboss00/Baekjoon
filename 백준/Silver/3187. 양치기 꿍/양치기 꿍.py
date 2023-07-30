"""
3187번. 양치기 꿍

같은 울타리 영역 안의 양들의 숫자가 늑대의 숫자보다
더 많을 경우 늑대가 잡아먹힘

울타리 : #
빈공간 : .
늑대 : v
양 : k

몇 마리의 양과 늑대가 살아남을 것인지?

벽이 아닐 경우
-> 탐색 진행
-> 늑대와 양의 갯수 세서
-> 더 많은 수를 리턴
"""
import sys
D = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x1, y1):
    v1, k1 = 0, 0
    # 늑대일 경우
    if board[y1][x1] == 'v':
        v1 += 1

    elif board[y1][x1] == 'k':
        k1 += 1

    # 방문 처리
    board[y1][x1] = '#'

    stack = []
    stack.append((x1,y1))

    while stack:
        x2, y2 = stack.pop()

        for dx, dy in D:
            nx = x2 + dx
            ny = y2 + dy

            if 0 <= nx < c and 0 <= ny < r:
                if board[ny][nx] != '#':
                    if board[ny][nx] == 'k':
                        k1 += 1
                    if board[ny][nx] == 'v':
                        v1 += 1
                    board[ny][nx] = '#'
                    stack.append((nx,ny))
    return (k1, 0) if k1 > v1 else (0, v1)

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
            k2, v2 = dfs(x,y)
            ans[0] += k2
            ans[1] += v2
print(*ans)