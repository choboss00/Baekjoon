"""
## 빙고

## 문제
1. 빙고 진행 방식
- 25개의 칸으로 이루어진 빙고판에 1 ~ 25까지 자연수를 한 칸에 하나씩 쓰기
- 사회자가 부르는 수를 차례로 지워나가기
- 차례로 수를 지우다가 같은 가로, 세로, 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋기
- 이러한 선이 3개 이상 그저이는 순간 빙고
- 가장 먼저 외치는 사람이 게임의 승자

2. 사회자가 몇 번째 수를 부른 후 철수가 빙고를 외치게 되는지 출력하기

## 입력
1. 1 ~ 5번째 줄까지 숫자

## 출력
1. 몇 번째 수를 부른 후 철수가 빙고를 외치게 되는지 출력하기

## 풀이
1. 게임판 만들기

2. 차례대로 번호를 탐색하며 하나씩 지우기

3. 위치에 맞게 탐색 진행
"""
import sys

input = sys.stdin.readline

board = []

visited_y = [False for _ in range(5)]
visited_x = [False for _ in range(5)]
visited_xy = [False, False]
cnt = 0
ans = 0

for _ in range(5):
    board.append(list(map(int, input().split())))

bingo_list = []

for _ in range(5):
    bingo_list.append(list(map(int, input().split())))

for bingos in bingo_list:
    for bingo in bingos:
        for y in range(5):
            for x in range(5):
                if board[y][x] == bingo:
                    board[y][x] = 'X'
                    cnt += 1

                    # 가로
                    if board[y].count('X') == 5 and not visited_y[y]:
                        ans += 1
                        visited_y[y] = True
                    # 세로
                    chx = 0
                    for i in range(5):
                        if board[i][x] == 'X':
                            chx += 1
                        else:
                            break
                    if chx == 5 and not visited_x[x]:
                        ans += 1
                        visited_x[x] = True # 방문처리

                    # 대각선
                    if x == y:
                        chx2 = 0
                        for i in range(5):
                            if board[i][i] == 'X':
                                chx2 += 1
                            else:
                                break

                        if chx2 == 5 and not visited_xy[0]:
                            ans += 1
                            visited_xy[0] = True

                    # 역대각선
                    if x == (4-y):
                        chx3= 0
                        for i in range(5):
                            if board[4-i][i] == 'X':
                                chx3 += 1
                            else:
                                break

                        if chx3 == 5 and not visited_xy[1]:
                            ans += 1
                            visited_xy[1] = True

                if ans >= 3:
                    print(cnt)
                    exit(0)


