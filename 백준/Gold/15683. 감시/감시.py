"""
## 감시

## 문제
1. 1 * 1 크기의 정사각형으로 나누어져 있는 N * M 크기의 직사각형

2. 사무실에는 총 K 개의 CCTV 가 설치되어 있음
- 종류 : 5가지
- 1번 : 한쪽 방향 감시
- 2번 : 서로 반대 방향 감시
- 3번 : 직각 방향 감시
- 4번 : 3방향 감시
- 5번 : 4방향 감시

3. CCTV 는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있음

4. 사무실에는 벽이 있는데, CCTV 는 벽을 통과할 수 없음
- CCTV 가 감시할 수 없는 영역 : 사각지대

5. CCTV 는 회전시킬 수 있음
- 회전은 항상 90도 방향으로 해야함
- 감시하려고 하는 방향은 가로 OR 세로

6. 지도
- 0 : 빈 칸
- 1 ~ 5 : CCTV
- 6 : 벽
- 감시할 수 있는 영역 : # 로 표시 ( 예시에서 )

7. CCTV 는 CCTV 를 통과할 수 있음 ( 빈 칸으로 보고 넘어갈 수 있음 )

8. 사무실의 크기와 상태, CCTV 의 정보가 주어졌을 때, CCTV 의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램 작성하기

## 입력
1. 사무실의 세로 크기 N, 가로 크기 M

2. 사무실 각 칸의 정보가 주어짐
- 0 : 빈 칸
- 1 ~ 5 : CCTV
- 6 : 벽
- CCTV 의 최대 개수는 8 개를 넘지 않음 ( 완전 탐색으로 돌아도 될듯 )

## 출력
1. 첫째 줄에 사각 지대의 최소 크기 출력하기

## 풀이
1. 사각 지대의 최소 크기를 구해야 함

2. CCTV 의 위치를 저장한 후, 완전 탐색

"""
import sys
from copy import deepcopy

_min = float("inf")

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

cctv_list = []
for y in range(n):
    for x in range(m):
        if 0 < board[y][x] < 6:
            cctv_list.append([board[y][x], x, y])

def cctv(board, x, y, flag):
    # 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while True:
        nx = x + dx[flag]
        ny = y + dy[flag]

        if 0 <= nx < m and 0 <= ny < n:
            if board[ny][nx] == 6:
                break
            elif board[ny][nx] == 0:
                board[ny][nx] = '#' # 벽 처리
            x, y = nx, ny
        else:
            break
    return board

def back(board, depth, level):
    global _min
    if level == depth:
        cnt = 0
        for y in range(n):
            for x in range(m):
                if board[y][x] == 0:
                    cnt += 1
        _min = min(_min, cnt)
        return

    temp_board = deepcopy(board)

    cctv_num, x, y = cctv_list[level]

    if cctv_num == 1:
        cctv1_left_board = cctv(temp_board, x, y, 0)
        back(cctv1_left_board, depth, level+1)
        temp_board = deepcopy(board)

        cctv1_right_board = cctv(temp_board, x, y, 1)
        back(cctv1_right_board, depth, level+1)
        temp_board = deepcopy(board)

        cctv1_up_board = cctv(temp_board, x, y, 2)
        back(cctv1_up_board, depth, level+1)
        temp_board = deepcopy(board)

        cctv1_down_board = cctv(temp_board, x, y, 3)
        back(cctv1_down_board, depth, level+1)
        temp_board = deepcopy(board)

    elif cctv_num == 2: # 상하, 좌우
        cctv2_left_right_board = cctv(cctv(temp_board, x, y, 0), x, y, 1)
        back(cctv2_left_right_board, depth, level+1)
        temp_board = deepcopy(board)

        cctv2_up_down_board = cctv(cctv(temp_board, x, y, 2), x, y, 3)
        back(cctv2_up_down_board, depth, level+1)
        temp_board = deepcopy(board)

    elif cctv_num == 3: # 직각
        cctv3_90_board = cctv(cctv(temp_board, x, y, 2), x, y, 1)
        back(cctv3_90_board, depth, level+1)
        temp_board = deepcopy(board)

        cctv3_180_board = cctv(cctv(temp_board, x, y, 1), x, y, 3)
        back(cctv3_180_board, depth, level+1)
        temp_board = deepcopy(board)

        cctv3_270_board = cctv(cctv(temp_board, x, y, 3), x, y, 0)
        back(cctv3_270_board, depth, level+1)
        temp_board = deepcopy(board)

        cctv3_360_board = cctv(cctv(temp_board, x, y, 0), x, y, 2)
        back(cctv3_360_board, depth, level+1)
        temp_board = deepcopy(board)

    elif cctv_num == 4: # 3방향
        cctv4_012_board = cctv(cctv(cctv(temp_board, x, y, 0), x, y, 1), x, y, 2)
        back(cctv4_012_board, depth, level+1)
        temp_board = deepcopy(board)

        cctv4_123_board = cctv(cctv(cctv(temp_board, x, y, 1), x, y, 2), x, y, 3)
        back(cctv4_123_board, depth, level+1)
        temp_board = deepcopy(board)

        cctv4_230_board = cctv(cctv(cctv(temp_board, x, y, 2), x, y, 3), x, y, 0)
        back(cctv4_230_board, depth, level+1)
        temp_board = deepcopy(board)

        cctv4_301_board = cctv(cctv(cctv(temp_board, x, y, 3), x, y, 0), x, y, 1)
        back(cctv4_301_board, depth, level+1)
        temp_board = deepcopy(board)

    elif cctv_num == 5: # 4방향
        cctv5 = cctv(cctv(cctv(cctv(temp_board, x, y, 0), x, y, 1), x, y, 2), x, y, 3)
        back(cctv5, depth, level+1)
        temp_board = deepcopy(board)


# board, depth, level, 감시 count
back(board, len(cctv_list), 0)

print(_min)
