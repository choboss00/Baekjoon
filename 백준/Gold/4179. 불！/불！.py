import sys
from collections import deque
def bfs():
    while fire_queue:
        x,y = fire_queue.popleft()

        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < c and 0 <= ny < r:
                if not fire[ny][nx] and board[ny][nx] != '#':
                    fire[ny][nx] = fire[y][x] + 1
                    fire_queue.append((nx,ny))

    while ji_queue:
        x, y = ji_queue.popleft()

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < c and 0 <= ny < r:
                if not ji[ny][nx] and board[ny][nx] != '#':
                    if not fire[ny][nx] or fire[ny][nx] > ji[y][x] + 1:
                        ji[ny][nx] = ji[y][x] + 1
                        ji_queue.append((nx,ny))
            else:
                return ji[y][x]

    return "IMPOSSIBLE"

input = sys.stdin.readline

r,c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

# 불의 위치, 지훈의 위치
fire = [[0 for _ in range(c)] for _ in range(r)]
ji = [[0 for _ in range(c)] for _ in range(r)]

fire_queue = deque()
ji_queue = deque()

for y in range(r):
    for x in range(c):
        if board[y][x] == 'F':
            fire[y][x] = 1
            fire_queue.append((x,y))
        if board[y][x] == 'J':
            ji[y][x] = 1
            ji_queue.append((x,y))

print(bfs())