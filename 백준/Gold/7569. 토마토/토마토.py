"""
7569번 토마토

토마토 : 익은 토마토, 안익은 토마토
익은 토마토에 인접한 안익은 토마토들은 하루가 지나면 익게 됨

방향 : 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 ( 6방향 )

창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 최소 일수 구하기

상자의 크기 : m * n ( m : 가로, n : 세로 )
상자의 수 : h

1 : 익은 토마토
0 : 익지 않은 토마토
-1 : 토마토가 들어있지 않은 칸

토마토가 모두 익을 때 까지 최소 며칠이 걸리는지 계산해서 출력하기

1인 경우를 찾고, bfs 탐색 진행

bfs 를 다 돌고, 현 board 에 0 이 있는지 찾기

"""
import sys
from collections import deque

D = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

def minus():
    for z1 in range(h):
        for y1 in range(n):
            for x1 in range(m):
                if board[z1][y1][x1] == 0:
                    return -1
    return 0

input = sys.stdin.readline

m,n,h = map(int, input().split())
cnt = 0
board = [[] for _ in range(h)]

queue = deque()

for z in range(h):
    for y in range(n):
        board[z].append(list(map(int, input().split())))
        for x in range(m):
            if board[z][y][x] == 1:
                queue.append((x,y,z,0))

while queue:
    x3,y3,z3,d3 = queue.popleft()

    for dx,dy,dz in D:
        nx = x3 + dx
        ny = y3 + dy
        nz = z3 + dz
        dd = d3

        # 예외 처리
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            # 다음 위치가 익지 않은 토마토일 경우
            if board[nz][ny][nx] == 0:
                queue.append((nx,ny,nz,dd+1))
                # 방문 처리
                board[nz][ny][nx] = 1
        if cnt < dd:
            cnt = dd

ans2 = minus()

if ans2 == -1:
    print(ans2)
else:
    print(cnt)

