"""
13565번. 침투 ( 실버 2 )

위 : outer side
아래 : inner side
격자 : 검은색 혹은 흰색
검은색 : 전류를 차단하는 물질
흰색 : 전류가 통할 수 있는 물질
전류 : 섬유 물질의 가장 바깥쪽 흰색 격자들에 공급
이후 상하좌우로 인접한 흰색 격자들로 전달 o

바깥쪽에서 흘려 준 정류가 안쪽까지 침투될 수 있는지
(outer side 출발 -> inner side 도착 )

0 : 전류가 잘 통하는 흰색
1 : 전류가 통하지 않는 검은색

가장 윗줄이 0 으로 시작하는 칸이 있어야함

마지만 칸 까지 도착할 경우, yes 출력
"""
import sys
from collections import deque

nx = [-1,1,0,0]
ny = [0,0,-1,1]
flag = False
def bfs(x1,y1):
    queue = deque()
    queue.append([x1,y1])
    # 방문표시
    board[y1][x1] = '@'

    while queue:
        x2, y2 = queue.popleft()

        for i in range(4):
            dx = x2 + nx[i]
            dy = y2 + ny[i]

            # 경계
            if 0 <= dx < m and 0 <= dy < n:
                # 갈 수 있는 길일경우
                if board[dy][dx] == '0':
                    queue.append([dx,dy])
                    # 방문표시
                    board[dy][dx] = '@'



input = sys.stdin.readline

# n : 세로, m : 가로
n,m = map(int, input().split())

board = []
# 지도 만들기
for _ in range(n):
    s = input().strip()
    s_list = []
    for i in s:
        s_list.append(i)
    board.append(s_list)

# 가장 윗부분에서 시작
for x in range(m):
    # 전류가 흐르는 칸이 있을 경우
    if board[0][x] == '0':
        # 그래프 탐색 진행
        bfs(x,0)

flag = False

for x1 in range(m):
    if board[-1][x1] == '@':
        flag = True
        break

if flag == True:
    print("YES")
else:
    print("NO")