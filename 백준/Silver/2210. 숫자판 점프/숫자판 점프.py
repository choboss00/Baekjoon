"""
숫자판 점프 ( 실버 2 )

5 * 5 크기의 숫자판

임의의 위치에서 시작해서 인접해있는 네방향으로 5번 이동하면서
각 칸에 적혀있는 숫자를 차례로 붙이면 6자리 수가 됨

이동할 때 한번 거쳤던 칸을 다시 거쳐도 됨

1. dfs 사용
2. 6자리수가 되면 종료
3. set() 으로 저장
"""
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans_set = set()

def dfs(x,y, ans):
    ans = ans + str(board[y][x])

    if len(ans) == 6:
        ans_set.add(ans)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 맵 안 부분만 탐색
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, ans)

input = sys.stdin.readline
# map
board = deque()
# 입력값 받기
for _ in range(5):
    board.append(list(map(int, input().split())))
# 탐색
for i in range(5):
    for j in range(5):
        dfs(j,i, "")

print(len(ans_set))