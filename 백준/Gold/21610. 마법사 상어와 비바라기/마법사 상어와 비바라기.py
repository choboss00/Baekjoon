N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 처음 비바라기 시전
magic = [[0 for _ in range(N)] for _ in range(N)]
# 비바라기 시전
magic[-1][0], magic[-1][1], magic[-2][0], magic[-2][1] = 1, 1, 1, 1

def direction_move_cloud(dx, dy):
    global magic, sub_magic
    for y in range(N):
        for x in range(N):
            if magic[y][x] == 1:
                magic[y][x] = 0
                new_y = (y + dy) % N
                new_x = (x + dx) % N
                sub_magic[new_y][new_x] = 1
    magic = sub_magic

def bug_magic(x, y):
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if board[ny][nx] > 0:
                board[y][x] += 1
def plus_water_and_delete_cloud(magic):
    delete_set = set()
    for y in range(N):
        for x in range(N):
            if magic[y][x] == 1:
                board[y][x] += 1
                # 구름 제거
                magic[y][x] = 0

                delete_set.add((x, y))
    return delete_set

def generate_cloud(delete_set):
    check_set = set()
    for y in range(N):
        for x in range(N):
            if board[y][x] >= 2:
                check_set.add((x,y))

    check_set = check_set - delete_set

    for x, y in check_set:
        board[y][x] -= 2
        magic[y][x] = 1


def move_cloud(d, s):
    global magic, sub_magic
    # 왼쪽으로 이동
    if d == 1:
        direction_move_cloud(-s, 0)
    # 왼쪽 위로 이동
    elif d == 2:
        direction_move_cloud(-s, -s)
    # 위로 이동
    elif d == 3:
        direction_move_cloud(0, -s)
    # 오른쪽 위로 이동
    elif d == 4:
        direction_move_cloud(s, -s)
    # 오른쪽으로 이동
    elif d == 5:
        direction_move_cloud(s, 0)
    # 오른쪽 아래로 이동
    elif d == 6:
        direction_move_cloud(s, s)
    # 아래로 이동
    elif d == 7:
        direction_move_cloud(0, s)
    # 왼쪽 아래로 이동
    elif d == 8:
        direction_move_cloud(-s, s)

    # 구름이 있는 칸의 바구니에 저장된 물의 양 + 1, 구름 제거, 물복사 버그 마법 시전
    delete_list = plus_water_and_delete_cloud(magic)

    # 물복사 버그 마법 사용
    for d in delete_list:
        bug_magic(d[0], d[1])

    # 구름 생성
    generate_cloud(delete_list)

for _ in range(M):
    d, s = map(int, input().split())

    sub_magic = [[0 for _ in range(N)] for _ in range(N)]

    move_cloud(d, s)

ans = 0

for y in range(N):
    for x in range(N):
        ans += board[y][x]

print(ans)