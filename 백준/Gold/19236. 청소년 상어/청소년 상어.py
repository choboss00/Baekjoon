import copy

board = []

# 맵 만들기
for _ in range(4):
    sub_list = list(map(int, input().split()))
    subsub_list = []
    for i in range(0, 8, 2):
        subsub_list.append(sub_list[i:i + 2])
    board.append(subsub_list)


def change_fish(board, d, dx, dy, x, y):
    nx = x + dx
    ny = y + dy

    if 0 <= nx < 4 and 0 <= ny < 4:
        # 상어가 아닐 경우 바꿀 수 있음
        if board[ny][nx][0] != -1:
            # 방향 전환 업데이트
            board[y][x][1] = d
            # 물고기 자리 교체
            board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
            return True  # 이동에 성공한 경우
    return False  # 이동에 실패한 경우


def direction_move_fish(board, d, x, y, cnt):
    if cnt == 9:
        return  # 종료
    # 위
    if d == 1:
        if not change_fish(board, d, 0, -1, x, y):
            direction_move_fish(board, d % 8 + 1, x, y, cnt + 1)
    # 왼쪽 위
    elif d == 2:
        if not change_fish(board, d, -1, -1, x, y):
            direction_move_fish(board, d % 8 + 1, x, y, cnt + 1)
    # 왼쪽
    elif d == 3:
        if not change_fish(board, d, -1, 0, x, y):
            direction_move_fish(board, d % 8 + 1, x, y, cnt + 1)
    # 왼쪽 아래
    elif d == 4:
        if not change_fish(board, d, -1, 1, x, y):
            direction_move_fish(board, d % 8 + 1, x, y, cnt + 1)
    # 아래
    elif d == 5:
        if not change_fish(board, d, 0, 1, x, y):
            direction_move_fish(board, d % 8 + 1, x, y, cnt + 1)
    # 오른쪽 아래
    elif d == 6:
        if not change_fish(board, d, 1, 1, x, y):
            direction_move_fish(board, d % 8 + 1, x, y, cnt + 1)
    # 오른쪽
    elif d == 7:
        if not change_fish(board, d, 1, 0, x, y):
            direction_move_fish(board, d % 8 + 1, x, y, cnt + 1)
    # 오른쪽 위
    elif d == 8:
        if not change_fish(board, d, 1, -1, x, y):
            direction_move_fish(board, d % 8 + 1, x, y, cnt + 1)


def move_fish(board):
    count = 1

    while count <= 16:
        for y in range(4):
            # 원하는 숫자를 찾았을 경우를 위한 bool
            check = False
            for x in range(4):
                if count == board[y][x][0]:
                    direction_move_fish(board, board[y][x][1], x, y, 1)
                    check = True
                    break
            # 원하는 숫자를 찾았을 때 바로 종료
            if check:
                break

        count += 1


def eat_fish(board, shark_x, shark_y, fish_x, fish_y):
    # 상어가 먹은 뒤 이동
    board[fish_y][fish_x][0] = -1
    # 이전 상어가 있던 장소는 초기화
    board[shark_y][shark_x][0] = 0


def can_eat_fishs(board, x, y, d):
    # 위
    fishs = []
    if d == 1:
        while y > 0:
            y -= 1
            if board[y][x][0] == 0:
                continue
            fishs.append([board[y][x][0], board[y][x][1], x, y])
    elif d == 2:
        while y > 0 and x > 0:
            y -= 1
            x -= 1
            if board[y][x][0] == 0:
                continue
            fishs.append([board[y][x][0], board[y][x][1], x, y])
    elif d == 3:
        while x > 0:
            x -= 1
            if board[y][x][0] == 0:
                continue
            fishs.append([board[y][x][0], board[y][x][1], x, y])
    elif d == 4:
        while x > 0 and y < 3:
            x -= 1
            y += 1
            if board[y][x][0] == 0:
                continue
            fishs.append([board[y][x][0], board[y][x][1], x, y])
    elif d == 5:
        while y < 3:
            y += 1
            if board[y][x][0] == 0:
                continue
            fishs.append([board[y][x][0], board[y][x][1], x, y])
    elif d == 6:
        while y < 3 and x < 3:
            x += 1
            y += 1
            if board[y][x][0] == 0:
                continue
            fishs.append([board[y][x][0], board[y][x][1], x, y])
    elif d == 7:
        while x < 3:
            x += 1
            if board[y][x][0] == 0:
                continue
            fishs.append([board[y][x][0], board[y][x][1], x, y])
    elif d == 8:
        while x < 3 and y > 0:
            x += 1
            y -= 1
            if board[y][x][0] == 0:
                continue
            fishs.append([board[y][x][0], board[y][x][1], x, y])
    return fishs


def eat_fishs(board, shark_x, shark_y, shark_dir):
    global ans
    # 상어가 먹을 수 있는 물고기 리스트 가져오기
    shark_eat_fishs = can_eat_fishs(board, shark_x, shark_y, shark_dir)
    copy_board = copy.deepcopy(board)

    for fish in shark_eat_fishs:
        eat_fish(board, shark_x, shark_y, fish[2], fish[3])
        ans += fish[0]
        ans_list.append(ans)
        # 물고기 이동
        move_fish(board)
        # 재귀 호출 ( 그 다음으로 이동 )
        eat_fishs(board, fish[2], fish[3], fish[1])
        # 이전 상태로 되돌리기
        board = copy.deepcopy(copy_board)
        ans -= fish[0]


# 상어가 물고기를 먹어야 함 : 초기엔 (0, 0) 좌표에 있는 물고기를 먹음
ans = board[0][0][0]
board[0][0][0] = -1
ans_list = []
ans_list.append(ans)

move_fish(board)

# 상어가 먹을 수 있는 물고기 중 하나를 먹음
eat_fishs(board, 0, 0, board[0][0][1])

print(max(ans_list))
