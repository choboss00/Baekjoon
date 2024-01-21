"""
## 치즈

## 문제
1. 정사각형 칸들로 이루어진 사각형 모양의 판

2. 그 위에 얇은 치즈가 놓여있음
- X : 치즈가 놓여있지 않음
- 치즈에는 하나 이상의 구멍이 있을 수 있음

3. 치즈를 공기 중에 놓으면 녹게 되는데, 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어짐
- 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 됨

4. 사각형 모양 칸의 크기와 한 조각의 치즈가 판 위에 주어졌을 때
- 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간
- 모두 녹기 1시간 전에 남아있는 치즈 조각이 놓여 있는 칸의 개수 구하기

## 입력
1. 세로, 가로의 길이

2. 치즈 X : 0, 치즈 O : 1

## 출력
1. 첫째 줄 : 치즈가 모두 녹아서 없어지는 데 걸리는 시간 출력

2. 둘째 줄 : 모두 녹기 1시간 전에 남아있는 치즈 조각이 놓여 있는 칸의 개수 출력하기

## 풀이
1. 여러 번의 BFS 탐색 진행
- 1번 탐색마다 겉 표면의 치즈 녹이기
- 표면 탐색

"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    visited = [[False for _ in range(m)] for _ in range(n)]

    visited[y][x] = True # 방문처리
    # return 할 치즈 리스트
    arr = []

    while queue:
        prev_x, prev_y = queue.popleft()

        for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
            nx = prev_x + dx
            ny = prev_y + dy

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx]:
                    # 현 위치가 0 일경우
                    if board[ny][nx] == 0:
                        visited[ny][nx] = True
                        queue.append([nx, ny])
                    else:
                        # 상하좌우 탐색
                        for ddx, ddy in [[-1,0], [1,0], [0,-1], [0,1]]:
                            nnx = nx + ddx
                            nny = ny + ddy

                            if 0 <= nnx < m and 0 <= nny < n:
                                if board[nny][nnx] == 0: # 빈 공간이 있을 경우
                                    arr.append([nx, ny]) # 녹아도 되는 치즈의 좌표
                                    visited[ny][nx] = True
                                    break
    return arr

# 시간, 마지막 치즈를 저장
time, ans = 0, 0

while True:
    # bfs 탐색 진행
    x, y = 0, 0
    arr = bfs(x, y)
    if len(arr) == 0:
        print(time)
        print(ans)
        break
    else:
        # 치즈 개수 저장
        ans = len(arr)
        time += 1
        for xx, yy in arr:
            board[yy][xx] = 0 # 벽으로 바꾸기
        x, y = arr[0][0], arr[0][1] # 초기화