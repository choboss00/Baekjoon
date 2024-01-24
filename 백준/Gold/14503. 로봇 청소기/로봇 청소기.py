"""
## 로봇 청소기

## 문제
1. 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수 구하기

2. 방 : N * M
- 1 * 1 크기의 정사각형 칸으로 나누어져 있음
- 벽, 혹은 빈칸
- 좌표 : (0, 0) ~ (N-1, M-1)
- 처음에 빈칸은 전부 청소되지 않은 상태

3. 청소기 : 바라보는 방향이 있음
- 동, 서, 남, 북 중 하나

4. 로봇 청소기 작동 방식
- 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
- 현재 칸의 주변 4칸중 청소되지 않은 빈칸이 없는경우 ( 상하좌우 다 청소 된 상태 )
- 바라보는 방향을 유지한 채로 한 칸을 후진할 수 있다면 1번 반복
- 후진할 수 없다면 종료

- 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
- 반시계 방향으로 90도 회전
- 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
- 1번 반복

## 입력
1. 방의 크기 : N * M

2. 초기 로봇 청소기의 좌표 (r, c), 방향 d
- d : 0 일 때 북, 1 일 때 동, 2 일 때 남, 3 일 때 서 ( 시계 방향 )

3. 각 장소의 상태를 나타내는 리스트
- 0 : 청소되지 않은 빈칸
- 1 : 벽
- 로봇 청소기가 있는 칸은 항상 빈칸

## 출력
1. 로봇 청소기가 작동을 시작한 후 작동을 멈출 때 까지 청소하는 칸의 개수 출력하기

## 풀이
1. 입력값 받기

2. 로봇 청소기의 초기 위치에서 작동 방식에 맞춰 동작
- 청소가 가능한 칸이 없는 경우 : 방향 유지 후 후진 or 종료
- 청소가 가능한 칸이 있는 경우 : 반시계 방향으로 회전 ( mod 연산을 하면 좋을 것 같음 )

3. 청소할 수 있는 칸 일경우, 갯수 카운트

"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# 로봇의 위치, 방향
# 방향은 0 : 북, 1 : 동, 2 : 남, 3 : 서
robot_y, robot_x, robot_dir = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

# 초기 위치
board[robot_y][robot_x] = 'X'
ans = 1
# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def checkClean(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if board[ny][nx] == 0: # 청소할 수 있는 칸 존재
                return True
    else:
        return False

while True:
    # 현재 칸 청소
    if board[robot_y][robot_x] == 0:
        ans += 1
        board[robot_y][robot_x] = 'X' # 방문처리

    # 청소되지 않은 칸이 존재할 경우
    if checkClean(robot_x, robot_y):
        robot_dir = (robot_dir + 3) % 4  # 반시계 방향으로 회전
        # 한칸 전진
        if board[robot_y + dy[robot_dir]][robot_x + dx[robot_dir]] == 0:
            robot_y = robot_y + dy[robot_dir]
            robot_x = robot_x + dx[robot_dir]
    else:
        if board[robot_y - dy[robot_dir]][robot_x - dx[robot_dir]] == 1: # 벽일경우
            print(ans)
            exit(0)
        else: # 1칸 후진
            robot_y = robot_y - dy[robot_dir]
            robot_x = robot_x - dx[robot_dir]


