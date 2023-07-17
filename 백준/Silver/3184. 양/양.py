"""
3184번. 양 ( 실버 1 )

. : 빈 필드
# : 울타리
o : 양
v : 늑대

한칸에서 수평, 수직만으로 이동
울타리를 지나지 않고 다른칸으로 이동 가능
-> 같은 영역

마당에서 탈출할 수 있는 칸은 어떤 영역에도 속하지 않는다고 간주

해결

1. bfs() 사용
- 늑대 수, 양 수 체크
- 방문 여부 체크

2. 늑대 수보다 양의 수가 더 많으면, 양 win
- 늑대 수 제거

3. 그렇지 않으면, 늑대 win
- 양 수 제거

4. 그러면 양 수, 늑대 수 총수를 체크해야함
"""
import sys
from collections import deque

nx = [-1,1,0,0]
ny = [0,0,-1,1]

# 양과 늑대 총 갯수
ov_sum = [0,0]
def bfs(x,y):
    # 초기 위치
    queue = deque()
    queue.append([x,y])
    # 현 위치에서 양의 수와 늑대의 수 체크
    o_1 = 0
    v_1 = 0
    if board[y][x] == 'o':
        o_1 += 1
    elif board[y][x] == 'v':
        v_1 += 1

    # 현 위치 방문처리
    board[y][x] = '#'

    while queue:
        x1, y1 = queue.popleft()

        for i in range(4):
            dx = x1 + nx[i]
            dy = y1 + ny[i]

            if 0 <= dx < c and 0 <= dy < r:
                # 아직 방문하지 않았을 경우
                if board[dy][dx] != '#':
                    # 양일 때
                    if board[dy][dx] == 'o':
                        o_1 += 1
                    elif board[dy][dx] == 'v':
                        v_1 += 1

                    # 방문표시
                    queue.append([dx, dy])
                    board[dy][dx] = '#'

    if o_1 > v_1:
        return [o_1,0]
    else:
        return [0,v_1]





input = sys.stdin.readline

# 입력값
r,c = map(int, input().split())
# map 만들기
board = []

for i in range(r):
    s = input().strip()
    s_list = []
    for j in s:
        s_list.append(j)
    board.append(s_list)

for y in range(r):
    for x in range(c):
        if board[y][x] != '#':
            a = bfs(x,y)
            ov_sum[0] += a[0]
            ov_sum[1] += a[1]


print(*ov_sum)