"""
11123번 : 양 한마리... 양 두마리... ( 실버 2 )

너비우선 탐색 ( bfs ) 진행
"""
import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x1,y1):
    queue = deque()

    queue.append([x1,y1])
    # 방문표시
    board[y1][x1] = '@'

    while queue:
        x2, y2 = queue.popleft()

        for i in range(4):
            nx = x2 + dx[i]
            ny = y2 + dy[i]

            # 범위 안이고 다음 위치가 양일경우
            if 0 <= nx < w and 0 <= ny < h:
                if board[ny][nx] == '#':
                    queue.append([nx,ny])
                    board[ny][nx] = '@'

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h,w = map(int, input().split())

    # 지도 만들기
    board = []

    # 양 무리 갯수 세기
    cnt = 0

    for _ in range(h):
        s = input().strip()
        s_list = []
        for i in s:
            s_list.append(i)
        board.append(s_list)

    for y in range(h):
        for x in range(w):
            if board[y][x] == '#':
                bfs(x,y)
                cnt += 1
    print(cnt)