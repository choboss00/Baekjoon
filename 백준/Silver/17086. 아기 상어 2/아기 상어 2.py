"""
17086번 : 아기 상어 2

1. N * M 크기의 공간에 아기 상어 여러 마리 존재
- 공간은 1 * 1 크기의 정사각형 칸으로 나누어져 있음
- 한 칸에는 아기 상어가 최대 1마리 존재함

2. 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리
- 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수
- 이동 : 8 방향

3. 안전 거리가 가장 큰 칸 구하기

입력
1. 공간의 크기 N, M

2. 공간의 상태
- 0 : 빈칸
- 1 : 아기 상어가 있는 칸

출력
1. 안전 거리의 최댓값 출력하기

풀이
1. BFS 탐색을 돌면서, 각 아기 상어마다 안전 거리 구하기
"""
import sys
from collections import deque

direction = [(-1,0), (1,0), (0,1), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]

def bfs(x, y):
    visited = [[-1] * m for _ in range(n)]
    queue = deque()
    queue.append((x,y))

    # 처음 위치
    visited[y][x] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            # 예외처리
            if 0 <= nx < m and 0 <= ny < n:
                # 현 위치가 아기상어 위치일 경우
                if visited[ny][nx] == -1 and board[ny][nx] == 1:
                    return visited[y][x] + 1

                # 방문하지 않은 곳 일 경우 == 0
                if visited[ny][nx] == -1 and board[ny][nx] == 0:
                    queue.append((nx,ny))
                    visited[ny][nx] = visited[y][x] + 1

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

sharks_list = []

for y in range(n):
    for x in range(m):
        if board[y][x] == 0:
            sharks_list.append(bfs(x,y))

if None in sharks_list:
    print(0)
else:
    print(max(sharks_list))
