"""
## 아기 상어

## 문제
1. N * N 크기의 공간에 물고기 M 마리와 아기 상어 1마리 존재
- 공간은 1 * 1 크기의 정사각형 칸으로 나눠져있음
- 한 칸에는 물고기가 최대 1마리 존재함

2. 가장 처음 아기 상어의 크기 : 2
- 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동함

3. 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없음
- 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있음

4. 아기 상어가 어디로 이동할지 결정하는 방법
- 더 이상 먹을 수 있는 물고기가 공간에 없다면, 아기 상어는 엄마 상어에게 도움을 요청함
( 전체 물고기 수를 카운트해야함 )
- 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러감
- 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러감

5. 거리 : 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸 개수의 최솟값

6. 거리가 가장 가까운 물고기가 많다면, 가장 위, 그러한 물고기가 여러마리라면, 가장 왼쪽
- 우선순위 : 위 -> 왼쪽

7. 이동 : 1초, 먹는데 걸리는 시간은 없음
- 이동과 동시에 물고기를 먹고, 그 칸은 빈칸이 됨

8. 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
- 크기가 2인경우, 2마리를 먹어야 3이 됨

9. 공간의 상태가 주어졌을 때, 아기 상어가 몇 초동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램 작성하기

## 입력
1. 공간의 크기 N

2. 공간의 상태
- 0 : 빈 칸
- 1 ~ 6 : 칸에 있는 물고기의 크기
- 9 : 아기 상어의 위치

## 풀이
1. BFS
- 문제의 조건에 맞게 bfs 탐색 진행
- while 문을 돌면서, bfs 탐색
- bfs 탐색의 return 값으로 물고기 배열 받기
"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 위치 저장
shark_x, shark_y = -1, -1
# 아기 상어 초기 크기
shark_size= 2
# 시간, 물고기 잡아먹은 수
t, cnt = 0, 0

for y in range(N):
    for x in range(N):
        if board[y][x] == 9: # 아기 상어의 위치
            shark_x, shark_y = x, y
            board[y][x] = 0
def bfs(x, y, size):
    queue = deque()

    queue.append([x, y])

    visited = [[-1 for _ in range(N)] for _ in range(N)]

    # 현 위치 방문처리
    visited[y][x] = 0

    # 먹을 수 있는 물고기 리턴
    fishs = []

    while queue:
        now_x, now_y = queue.popleft()

        for xx, yy in [[-1,0], [1,0], (0,1), (0,-1)]:
            nx = xx + now_x
            ny = yy + now_y

            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == -1:
                if board[ny][nx] <= size: # 지나갈 수 있을 때
                    queue.append([nx, ny])
                    visited[ny][nx] = visited[now_y][now_x] + 1

                    if board[ny][nx] < size and board[ny][nx] != 0: # 먹을 수 있을 때
                        fishs.append([nx, ny, visited[ny][nx]])

    return fishs




while True:
    fishs = bfs(shark_x, shark_y, shark_size)

    # 먹을 수 있는 물고기가 없을 경우 종료
    if len(fishs) == 0:
        break

    fishs.sort(key=lambda x : (x[2], x[1], x[0]))

    # 정렬된 결괏값 중 가장 가까이 있는 물고기 가져오기
    nx, ny, dist = fishs.pop(0)

    t += dist # 1칸당 시간 1초

    board[shark_y][shark_x], board[ny][nx] = 0, 0 # 좌표 초기화 ( 먹었으니 )
    shark_x, shark_y = nx, ny # 먹은 물고기 좌표로 아기 상어 이동

    # 물고기 먹었으니 크기 증가
    cnt += 1

    if cnt == shark_size:
        shark_size += 1
        cnt = 0

print(t)