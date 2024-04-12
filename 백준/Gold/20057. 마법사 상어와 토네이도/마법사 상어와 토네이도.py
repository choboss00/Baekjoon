N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
# 가운데
x, y = N // 2, N // 2
# 처음 크기
size = [1,0]
# 처음 방향 ( 왼 - 아래 - 오른 - 위 )
d = 0
# 격자 밖으로 나간 모래의 양
ans = 0

def sand_storm(nx, ny):
    global ans
    # 현재 모래의 양
    sand = board[ny][nx]
    a = 0
    # 왼쪽
    if d == 0:
        for dx, dy in ((0, -1), (0, -2), (0, 1), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0)):
            nnx = nx + dx
            nny = ny + dy

            per = 0

            if (dx, dy) in [(0, -1), (0, 1)]:
                per = 7
            elif (dx, dy) in [(0, -2), (0, 2)]:
                per = 2
            elif (dx, dy) in [(-1, -1), (-1, 1)]:
                per = 10
            elif (dx, dy) in [(1, -1), (1, 1)]:
                per = 1
            elif (dx, dy) == (-2, 0):
                per = 5

            if 0 <= nnx < N and 0 <= nny < N:
                board[nny][nnx] += (sand * per // 100)
                a += (sand * per // 100)
            else:
                ans += (sand * per // 100)
                a += (sand * per // 100)

        if 0 <= nx-1 < N and 0 <= ny < N:
            board[ny][nx-1] += (sand - a)
        else:
            ans += (sand - a)
    # 아래
    elif d == 1:
        for dx, dy in ((-1, 0), (1, 0), (-2, 0), (2, 0), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 2)):
            nnx = nx + dx
            nny = ny + dy

            per = 0

            if (dx, dy) in [(-1, 0), (1, 0)]:
                per = 7
            elif (dx, dy) in [(-2, 0), (2, 0)]:
                per = 2
            elif (dx, dy) in [(-1, -1), (1, -1)]:
                per = 1
            elif (dx, dy) in [(-1, 1), (1, 1)]:
                per = 10
            elif (dx, dy) == (0, 2):
                per = 5

            if 0 <= nnx < N and 0 <= nny < N:
                board[nny][nnx] += (sand * per // 100)
                a += (sand * per // 100)
            else:
                ans += (sand * per // 100)
                a += (sand * per // 100)

        if 0 <= nx < N and 0 <= ny + 1 < N:
            board[ny+1][nx] += (sand - a)
        else:
            ans += (sand - a)
    # 오른쪽
    elif d == 2:
        for dx, dy in ((0, -1), (0, -2), (0, 1), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1), (2, 0)):
            nnx = nx + dx
            nny = ny + dy

            per = 0

            if (dx, dy) in [(0, -1), (0, 1)]:
                per = 7
            elif (dx, dy) in [(0, -2), (0, 2)]:
                per = 2
            elif (dx, dy) in [(-1, -1), (-1, 1)]:
                per = 1
            elif (dx, dy) in [(1, -1), (1, 1)]:
                per = 10
            elif (dx, dy) == (2, 0):
                per = 5

            if 0 <= nnx < N and 0 <= nny < N:
                board[nny][nnx] += (sand * per // 100)
                a += (sand * per // 100)
            else:
                ans += (sand * per // 100)
                a += (sand * per // 100)

        if 0 <= nx+1 < N and 0 <= ny < N:
            board[ny][nx+1] += (sand - a)
        else:
            ans += (sand - a)
    elif d == 3:
        for dx, dy in ((-1, 0), (1, 0), (-2, 0), (2, 0), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, -2)):
            nnx = nx + dx
            nny = ny + dy

            per = 0

            if (dx, dy) in [(-1, 0), (1, 0)]:
                per = 7
            elif (dx, dy) in [(-2, 0), (2, 0)]:
                per = 2
            elif (dx, dy) in [(-1, -1), (1, -1)]:
                per = 10
            elif (dx, dy) in [(-1, 1), (1, 1)]:
                per = 1
            elif (dx, dy) == (0, -2):
                per = 5

            if 0 <= nnx < N and 0 <= nny < N:
                board[nny][nnx] += (sand * per // 100)
                a += (sand * per // 100)
            else:
                ans += (sand * per // 100)
                a += (sand * per // 100)

        if 0 <= nx < N and 0 <= ny-1 < N:
            board[ny-1][nx] += (sand - a)
        else:
            ans += (sand - a)
    # 기존 모래는 다 날아감
    board[ny][nx] = 0
    # 현재 격자밖으로 나간 모래 체크
def move_direction_tornado(dx, dy):
    global x, y

    for i in range(1, size[0]+1):
        nx = x + dx * i
        ny = y + dy * i

        if 0 <= nx < N and 0 <= ny < N:
            # 모래바람 계산하기
            sand_storm(nx, ny)
    # 위치 업데이트
    x = nx
    y = ny

def move_tornado(d):
    # 왼쪽
    if d == 0:
        move_direction_tornado(-1, 0)
    elif d == 1:
        move_direction_tornado(0, 1)
    elif d == 2:
        move_direction_tornado(1, 0)
    elif d == 3:
        move_direction_tornado(0, -1)

    # 다음 방향으로 이동
    d = (d + 1) % 4
    return d
def size_up():
    size[1] += 1

    if size[1] == 2:
        size[0] += 1
        size[1] = 0

for _ in range(N * 2 - 1):
    # 토네이도 이동
    d = move_tornado(d)

    # 사이즈 업
    size_up()

print(ans)