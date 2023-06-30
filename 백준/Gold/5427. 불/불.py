"""
5427번. 불 ( 골드 4 )

매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나감
벽에는 불이 안붙음

상근 : 동서남북 인접 칸 이동 가능 ( 1초 소요 )
벽 통과 X, 불이 옮겨진 칸 OR 이제 불이 붙으려는 칸으로 이도 ㅇX

상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동 가능

빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지
구하는 프로그램 작성하기

. : 빈공간
# : 벽
@ : 상근이의 시작 위치
* : 불

맵 밖으로 나가면 탈출
다 * 표시 일 경우, 불가능
숫자 존재 -> 가능
"""
import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():

    while queue:
        x,y = queue.popleft()
        if visited[x][y] != 'FIRE':
            flag = visited[x][y]
        else:
            flag = "FIRE"

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == -1 and (map_list[nx][ny] == "." or map_list[nx][ny] == '@'):
                    if flag == "FIRE":
                        visited[nx][ny] = flag
                    else:
                        visited[nx][ny] = flag + 1
                    queue.append([nx,ny])
            else:
                if flag != "FIRE":
                    return flag + 1
    return "IMPOSSIBLE"

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    w,h = map(int, input().split())
    queue = deque()

    map_list = []
    visited = [[-1] * w for _ in range(h)]

    for i in range(h):
        map_list.append(list(input().strip()))
        for j in range(w):
            if map_list[i][j] == "@":
                visited[i][j] = 0
                s = [i,j]
            elif map_list[i][j] == "*":
                visited[i][j] = "FIRE"
                queue.append([i,j])
    queue.append(s)

    print(bfs())