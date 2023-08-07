import sys
from collections import deque
def bfs():
    while queue:
        # x,y,바이러스,시간
        x2, y2, c2, s2 = queue.popleft()
        if s2 == s:
            return board[x - 1][y - 1]

        for i in range(4):
            nx = x2 + dx[i]
            ny = y2 + dy[i]
            # 현재 s 초에서 바이러스가 다 퍼졌을 때
            if 0 <= nx < n and 0 <= ny < n:
                # 갈 수 있을 경우
                if board[ny][nx] == 0:
                    for k1 in range(1, k+1):
                        if c2 == k1:
                            queue.append((nx,ny,c2,s2+1))
                            board[ny][nx] = k1


input = sys.stdin.readline

n,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# s : 시간, x,y : 좌표
s,x,y = map(int, input().split())
check_list = [i for i in range(1, k+1)]
sub_list = []
for y1 in range(n):
    for x1 in range(n):
        for c1 in range(k):
            if board[y1][x1] == check_list[c1]:
                sub_list.append([x1,y1,board[y1][x1], 0])

# 정렬
sub_list.sort(key=lambda x:x[2])

queue = deque(sub_list)

if len(queue) == 0:
    print(0)
    exit(0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = bfs()
if ans == None:
    print(board[x-1][y-1])
else:
    print(ans)