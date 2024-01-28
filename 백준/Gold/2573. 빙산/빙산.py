"""
## 빙산

## 문제
1. 빙산의 각 부분별 높이 정보 : 배열의 각 칸에 양의 정수로 저장됨
- 빙산 이외의 바다에 해당하는 칸 : 0 이 저장됨

2. 바닷물에 접해있는 부분 : 1년마다 그 칸에 동서남북 4방향으로 붙어있는 0 이 저장된 칸의 개수만큼 줄어듬
- 각 칸에 저장된 높이는 0보다 더 줄어들지 않음

3. 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간을 구하는 프로그램 작성하기
- 만약 전부 다 녹을 때 까지 두 덩어리 이상으로 분리되지 않으면, 프로그램은 0 을 출력함

## 입력
1. 행, 열 ( N, M )

2. 배열의 첫번째 행, 열, 마지막 행, 열은 항상 0 으로 채워짐

## 출력
1. 빙산이 분리되는 최초의 시간을 출력하기

2. 만약 빙산이 다 녹을 때 까지 분리되지 않으면 0 출력

## 풀이
1. 빙산의 위치에서 4방향 ( 동 서 남 북 ) 체크 하기

2. 체크 후, 빙산의 X 좌표, Y 좌표와 4방향 바닷물 카운트한 배열 리턴하기

3. 한번 녹인 후, 빙산이 2개 이상으로 분리되었는지 체크하기
- 분리가 된 경우, 시간 출력하기
- 만약 빙산이 다 녹을 때 까지 분리되지 않은 경우 0 출력하기

"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def bfs(x, y):
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]

    queue.append([x, y])
    visited[y][x] = True # 방문 처리

    arr = []

    while queue:
        pr_x, pr_y = queue.popleft()

        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx = pr_x + dx
            ny = pr_y + dy

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx]:
                    if board[ny][nx] != 0:
                        ww = 0 # 바닷물 카운트
                        # 현 위치에서 동서남북 탐색
                        for dxx, dyy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                            nxx, nyy = nx + dxx, ny + dyy

                            if 0 <= nxx < m and 0 <= nyy < n:
                                if board[nyy][nxx] == 0: # 주변이 바다일 경우
                                    ww += 1

                        arr.append([nx, ny, ww])
                        queue.append([nx, ny])
                        visited[ny][nx] = True # 방문처리
                    else: # 바닷물일경우
                        queue.append([nx, ny])
                        visited[ny][nx] = True
        x, y = pr_x, pr_y

    return arr, x, y

def bfs2(x, y, visited): # 빙산 체크
    global two_check

    queue = deque()
    queue.append([x, y])

    visited[y][x] = True # 방문 처리
    two_check += 1

    while queue:
        pr_x, pr_y = queue.popleft()

        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx = pr_x + dx
            ny = pr_y + dy

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx]:
                    if board[ny][nx] != 0:
                        queue.append([nx, ny])
                        visited[ny][nx] = True

while True:
    prev_x, prev_y = 0, 0

    # 빙산이 2개 이상으로 갈라졌는지 체크
    two_check = 0

    waters, now_x, now_y = bfs(prev_x, prev_y) # bfs 탐색 진행

    # 초기화
    prev_x, prev_y = now_x, now_y

    # 1 사이클 돌기
    for x, y, water in waters:
        if board[y][x] - water > 0:
            board[y][x] -= water
        else:
            board[y][x] = 0

    ans += 1

    visited = [[False for _ in range(m)] for _ in range(n)]

    # 빙산이 2개로 나눠졌는지에 대한 bfs 탐색 진행
    for y in range(n):
        for x in range(m):
            if board[y][x] != 0 and not visited[y][x]:
                bfs2(x, y, visited)

    # 만약 리스트가 비어있을 경우, 다 2개 이상으로 쪼개지지 않고 다 녹았다는 뜻
    if len(waters) == 0:
        print(0)
        exit(0)


    if two_check >= 2:
        print(ans)
        exit(0)
