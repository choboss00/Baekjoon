"""
상범 빌딩 ( 골드 5 )

상범 빌딩에서 탈출하기
상범 빌딩 : 각 변의 길이가 1인 정육면체로 이루어져있음
각 정육면체는 금으로 이루어져 있어 지나갈 수 없거나, 비어있어서 지나갈 수 있게 되어있음 ( 0 , 1 )
각 칸에서 6개의 칸 ( 동 서 남 북 위 아래 ) 으로 1분의 시간을 들여 이동할 수 있음 -> 대각선 불가능

탈출 여부 / 시간 얼마나 걸리는지 출력하기

입력
L,R,C = 층, 행, 열

입력의 끝 : 0 0 0
시작 지점과 출구는 항상 하나만 존재

출력
Escaped in x minutes(s).

탈출 불가능 -> Trapped!

풀이 -> bfs 를 이용해서 위 아래 탐색을 어떻게 할 것인지?
현 위치에서 위아래 탐색도 추가해버리기
"""
import sys
from collections import deque

# 갈 수 있는 방향 표시
D = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)]

def bfs(x1, y1, z1):
    queue = deque()
    queue.append((x1, y1, z1))

    # 방문 표시
    board[z1][y1][x1] = 0

    while queue:
        x2,y2,z2 = queue.popleft()

        for dx,dy,dz in D:
            nx = x2 + dx
            ny = y2 + dy
            nz = z2 + dz

            # 예외처리
            if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L:
                # 현 위치가 도착 지점 일 경우
                if board[nz][ny][nx] == 'E':
                    return board[z2][y2][x2] + 1
                # 갈 수 있는 길일경우
                if board[nz][ny][nx] == '.':
                    queue.append((nx,ny,nz))

                    # 방문 표시
                    board[nz][ny][nx] = board[z2][y2][x2] + 1
    return -1

def solve():
    for z in range(L):
        for y in range(R):
            for x in range(C):
                if board[z][y][x] == 'S':
                    ans = bfs(x,y,z)
                    if ans == -1:
                        return 'Trapped!'
                    else:
                        return f'Escaped in {ans} minute(s).'

input = sys.stdin.readline

# 입력 ( 층, 행, 열 )
while True:
    L,R,C = map(int, input().split())
    # 종료 조건
    if L == 0 and R == 0 and C == 0:
        break
    # 아파트
    board = []
    # 3차원 배열
    for z in range(L):
        # 한 층씩 저장
        z_list = []
        for y in range(R):
            s = input().strip()
            y_list = []
            for i in s:
                y_list.append(i)
            z_list.append(y_list)
        board.append(z_list)
        # 띄어쓰기 입력 받기
        jump = input()

    print(solve())
