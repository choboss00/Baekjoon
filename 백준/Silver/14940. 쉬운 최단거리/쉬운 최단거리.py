"""
14940번 쉬운 최단거리

지도의 크기 n, m
n : 세로
m : 가로

0 : 갈 수 없는 땅
1 : 갈 수 있는 땅
2 : 목표지점

출력 : 각 지점에서 목표지점까지의 거리 출력하기
갈 수 없는 땅 ( 0 ) 인 경우, 0 그대로 출력
갈 수 있는 땅인 부분 중에서 2 에 도달할 수 없는 위치는 -1 출력
"""
import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x1,y1):
    queue = deque()
    queue.append([x1,y1])

    while queue:
        x2, y2 = queue.popleft()

        for i in range(4):
            nx = x2 + dx[i]
            ny = y2 + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                # 아직 방문하지 않은 경우
                if visited[ny][nx] == -1:
                    queue.append([nx,ny])
                    visited[ny][nx] = visited[y2][x2] + 1


input = sys.stdin.readline
# n : 세로, m : 가로
n,m = map(int, input().split())

board = []

for i in range(n):
    board.append(list(map(int, input().split())))

visited = [[-1 for _ in range(m)] for _ in range(n)]

# 목표지점 저장할 값
a,b = 0,0

for y in range(n):
    for x in range(m):
        # 갈 수 없는 땅 표시
        if board[y][x] == 0:
            visited[y][x] = 0
        # 위치 표시
        elif board[y][x] == 2:
            visited[y][x] = 0
            a,b = x,y
bfs(a,b)

for y in range(n):
    for x in range(m):
        print(visited[y][x], end=' ')
    print()