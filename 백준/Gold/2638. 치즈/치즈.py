from collections import deque

def make_set():
    return_set = set()

    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                return_set.add((x, y))
    #print(f"리턴할 치즈가 들어있는 집합 세트 : {return_set}")
    return return_set

def bfs():
    global cheese_set

    ans = 0
    while cheese_set:
        minus_cheese_set = set()

        for x, y in cheese_set:
            cnt = 0
            # 4방향 탐색
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nx = x + dx
                ny = y + dy

                if 0 <= nx < M and 0 <= ny < N:
                    if board[ny][nx] == 2:
                        cnt += 1

            if cnt >= 2:
                minus_cheese_set.add((x, y))

        # 녹은 치즈
        for mx, my in minus_cheese_set:
            find_outside_paper(mx, my)

        #print(f"현재 녹은 치즈 목록 : {minus_cheese_set}")
        cheese_set = cheese_set - minus_cheese_set
        ans += 1

    return ans

def find_outside_paper(x, y):
    queue = deque()

    queue.append([x, y])
    # 바깥 처리
    visited[y][x] = True
    board[y][x] = 2

    while queue:
        x1, y1 = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = x1 + dx
            ny = y1 + dy

            if not visited[ny][nx] and board[ny][nx] == 0: # 바깥일경우
                board[ny][nx] = 2
                visited[ny][nx] = True
                queue.append([nx, ny])

    #print(f"바깥 처리 후 : {board}")

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 바깥인지 안인지 구분짓는 방문처리
visited = [[False for _ in range(M)] for _ in range(N)]

# 바깥인지 안인지 구분짓기
find_outside_paper(0, 0)

cheese_set = make_set()

#print(f"현재 치즈가 들어있는 집합 세트 : {cheese_set}")

print(bfs())


