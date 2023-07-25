"""
1388번. 바닥 장식 ( 실버 4 )

-- 의 경우 같은 나무 판자
방 바닥을 장식하는데 필요한 나무 판자의 개수 출력하기
"""

from collections import deque
import sys

# 이동 표시
dx = [-1,1]
dy = [-1,1]
def bfs1(x1,y1):
    queue = deque()
    queue.append([x1,y1])

    # 방문 표시
    board[y1][x1] = 'A'

    while queue:
        x2, y2 = queue.popleft()

        for i in range(2):
            nx = x2 + dx[i]
            if 0 <= nx < m:
                if board[y2][nx] == '-':
                    queue.append([nx,y2])
                    board[y2][nx] = 'A'

def bfs2(x1,y1):
    queue = deque()
    queue.append([x1, y1])

    # 방문 표시
    board[y1][x1] = 'B'

    while queue:
        x2, y2 = queue.popleft()

        for i in range(2):
            ny = y2 + dy[i]
            if 0 <= ny < n:
                if board[ny][x2] == '|':
                    queue.append([x2, ny])
                    board[ny][x2] = 'B'

input = sys.stdin.readline
# 세로 : n, 가로 : m
n,m = map(int, input().split())

board = []

for i in range(n):
    s = input().strip()
    s_list = []
    for j in s:
        s_list.append(j)
    board.append(s_list)

# 갯수
cnt = 0

for y in range(n):
    for x in range(m):
        if board[y][x] == '-':
            bfs1(x,y)
            cnt += 1
        elif board[y][x] == '|':
            bfs2(x,y)
            cnt += 1

print(cnt)