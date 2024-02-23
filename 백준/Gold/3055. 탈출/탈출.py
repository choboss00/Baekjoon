"""
## 탈출

## 문제
1. 지도 : R행 C열
- 비어있는 곳 : '.'
- 물이 차있는 지역 : '*'
- 돌 : 'X'
- 비버의 굴 : 'D'
- 고슴도치의 위치 : 'S'

2. 매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있음
- 위, 아래, 오른쪽, 왼쪽

3. 물도 매 분마다 비어있는 칸으로 확장함
- 물이 있는 칸과 비어있는 칸은 물이 차게 됨

4. 물과 고슴도치는 돌을 통과할 수 없음

5. 고슴도치는 물로 차있는 구역으로 이동할 수 없음
- 물도 비버의 소굴로 이동할 수 없음

6. 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간 구하기

7. 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없음

## 입력
1. R, C

2. 지도
- D, S는 하나씩만 주어짐

## 출력
1. 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간 출력하기

2. 비버의 굴로 이동할 수 없는 경우, KAKTUS 출력하기

## 풀이
1. BFS
- 물이 차있는 지역과 고슴도치의 위치를 같이 BFS 탐색
"""
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(input().strip()) for _ in range(r)]
visited = [[-1 for _ in range(c)] for _ in range(r)]
queue = deque()

for y in range(r):
    for x in range(c):
        if board[y][x] == '*':
            queue.appendleft([x, y, board[y][x]])
            visited[y][x] = '*'
        elif board[y][x] == 'S':
            queue.append([x, y, board[y][x]])
            visited[y][x] = 0

while queue:
    x, y, now = queue.popleft()

    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < c and 0 <= ny < r:
            if now == '*': # 현재 비일경우
                if visited[ny][nx] == -1 and board[ny][nx] == '.': # 아직 방문하지 않았을 경우
                    queue.append([nx, ny, "*"])
                    visited[ny][nx] = '*' # 비로 침식
            elif now == 'S': # 고슴도치
                if board[ny][nx] == 'D':
                    print(visited[y][x] + 1)
                    exit(0)

                if visited[ny][nx] == -1 and board[ny][nx] == '.':
                    queue.append([nx, ny, "S"])
                    visited[ny][nx] = visited[y][x] + 1

print('KAKTUS')