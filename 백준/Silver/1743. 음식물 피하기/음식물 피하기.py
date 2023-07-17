"""
1743번. 음식물 피하기 ( 실버 1 )

1. 제일 큰 음식물의 크기 구하기
-> map 그리기
-> 음식물 표시하기

2. bfs 탐색해서 최대 개수 구하기
"""
import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x1,y1):
    queue = deque()
    queue.append([x1,y1])

    # 방문처리
    board[y1][x1] = '@'
    # 갯수
    cnt = 1

    while queue:
        x2, y2 = queue.popleft()

        for i in range(4):
            nx = x2 + dx[i]
            ny = y2 + dy[i]

            # 예외 처리
            if 0 <= nx < x and 0 <= ny < y:
                if board[ny][nx] == '#':
                    # 갯수 증가
                    cnt += 1

                    queue.append([nx,ny])
                    board[ny][nx] = '@'
    return cnt



input = sys.stdin.readline
y,x,k = map(int, input().split())

ans_list = []
# board 에 표시하기
board = [['.' for _ in range(x)] for _ in range(y)]

for _ in range(k):
    a,b = map(int, input().split())

    # 위치 조정
    a -= 1
    b -= 1

    board[a][b] = '#'
for i in range(y):
    for j in range(x):
        if board[i][j] == '#':
            ans_list.append(bfs(j,i))

print(max(ans_list))

