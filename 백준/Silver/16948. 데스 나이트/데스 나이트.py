"""
16948번. 데스 나이트 ( 실버 1 )

방향 설정 후 최소 이동 횟수 구하기
이동할 수 없는 경우, -1 출력하기
"""
from collections import deque
import sys

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(x1,y1,x2,y2):
    queue = deque()
    queue.append([x1,y1])

    # 방문 표시
    board[y1][x1] = 0
    cnt = 0

    while queue:
        x3, y3 = queue.popleft()

        for i in range(6):
            nx = x3 + dx[i]
            ny = y3 + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 현재 방문 지점이 1 일 경우
                if board[ny][nx] == -1:
                    queue.append([nx,ny])
                    # 방문 표시
                    board[ny][nx] = board[y3][x3] + 1




input = sys.stdin.readline

n = int(input())

r1,c1,r2,c2 = map(int, input().split())

# 지도 만들기
board = [[-1 for i in range(n)] for i in range(n)]

bfs(r1,c1,r2,c2)

print(board[c2][r2])