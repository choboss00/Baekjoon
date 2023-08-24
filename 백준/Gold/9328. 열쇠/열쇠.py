import sys
from collections import deque
from string import ascii_uppercase
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
    global answer
    queue = deque()
    queue.append(start)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < H and 0 <= ay < W and board[ax][ay] != "*" and not visited[ax][ay]: #방문할 수 있는 경우
                if board[ax][ay].isupper(): # 문인 경우
                    if board[ax][ay] in key: # 열쇠가 있다면 방문
                        queue.append([ax, ay])
                        visited[ax][ay] = True
                    else: # 열쇠가 없다면 미방문 좌표로 저장
                        unlocked_door[board[ax][ay]].append([ax, ay])
                else: # 통로, 문서, 열쇠인 경우
                    queue.append([ax,ay])
                    visited[ax][ay] = True
                    if board[ax][ay] == "$": # 문서인 경우
                        answer += 1
                    if board[ax][ay].islower(): # 열쇠인 경우
                        key.add(board[ax][ay].upper()) # 열쇠흘 저장
                        for x1, y1 in unlocked_door[board[ax][ay].upper()]: # 해당 열쇠로 열 수 있는 미방문 좌표를 방문
                            queue.append([x1, y1])
                            visited[x1][y1] = True


for _ in range(int(input())):
    answer = 0
    H,W = map(int,input().split())
    board = [list(input().strip()) for _ in range(H)]
    key = set()
    unlocked_door = dict()
    for alphabet in ascii_uppercase:
        unlocked_door[alphabet] = []
    start = []
    for k in input().strip():
        if k == "0":
            break
        key.add(k.upper())
    visited = [[False for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == 0 or i == H-1 or j == 0 or j == W-1: # 테투리인 경우
                if board[i][j] != "*":
                    if board[i][j].isupper(): # 문인 경우 미방문 좌표로 저장
                        unlocked_door[board[i][j]].append([i, j])
                    else: # 아닌 경우 문서, 열쇠, 통로의 경우로 나누어서 처리
                        if board[i][j] == "$":
                            answer += 1
                        elif board[i][j].islower():
                            key.add(board[i][j].upper())
                        start.append([i,j])
                        visited[i][j] = True
    for k in key: # 지금 갖고있는 열쇠로 방문할 수 있는 미방문 좌표 탐색
        for x,y in unlocked_door[k]:
            start.append([x,y])
            visited[x][y] = True
    for s in start: # 테두리의 가능한 시작좌표에 대해 탐색시작
        bfs(s)
    print(answer)