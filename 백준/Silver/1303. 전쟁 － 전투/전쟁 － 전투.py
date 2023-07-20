"""
1303번. 전쟁 - 전투 ( 실버 1 )

우리팀 : 흰옷
적팀 : 파란옷

-> 병사들이 모일수록 강해짐
n명이 뭉쳐있으면 n^2 의 위력을 낼 수 있음

우리팀, 적팀의 병사의 위력 합 출력하기

"""
import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x1,y1):
    queue = deque()
    queue.append([x1,y1])
    # 체크표시
    check = True
    if board[y1][x1] == 'W':
        check = True
    elif board[y1][x1] == 'B':
        check = False
    # 방문표시
    board[y1][x1] = '@'

    # 갯수
    cnt = 1

    while queue:
        x2, y2 = queue.popleft()

        for i in range(4):
            nx = x2 + dx[i]
            ny = y2 + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 현재 방문 지점 체크
                if check:
                    if board[ny][nx] == 'W':
                        queue.append([nx,ny])
                        cnt += 1

                        board[ny][nx] = '@'
                elif not check:
                    if board[ny][nx] == 'B':
                        queue.append([nx,ny])
                        cnt += 1

                        board[ny][nx] = '@'

    return cnt




input = sys.stdin.readline

n,m = map(int, input().split())

board = []
# 맵 만들기
for _ in range(m):
    s = input().strip()
    s_list = []
    for i in s:
        s_list.append(i)
    board.append(s_list)

# 위력 저장
cnt1, cnt2 = 0,0

for y in range(m):
    for x in range(n):
        if board[y][x] == 'W':
            cnt1 += bfs(x,y) ** 2
        elif board[y][x] == 'B':
            cnt2 += bfs(x,y) ** 2

print(cnt1, cnt2)