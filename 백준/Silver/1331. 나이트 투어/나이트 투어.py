"""
## 나이트 투어

## 문제
1. 체스판에서 나이트가 모든 칸을 정확히 한 번씩 방문하며, 마지막으로 방문하는 칸에서 시작점으로 돌아올 수 있는 경로

2. 6 * 6 의 크기
- 체스판의 한 칸은 A, B, C, D, E, F 중에서 하나와 1, 2, 3, 4, 5, 6 중에서 하나를 이어붙인 것으로 나타낼 수 있음
- A, B, C, D, E, F : 가로
- 1, 2, 3, 4, 5, 6 : 세로

3. 나이트 투어 경로가 주어질 때, 이것이 올바른 것이면 Valid, 그렇지 않으면 Invalid 를 출력하는 프로그램 작성하기

## 입력
1. 나이트가 방문한 순서대로 입력이 주어짐

## 출력
1. 문제의 정답 출력하기

## 풀이
1. 방문 기록 남기기

"""
import sys

input = sys.stdin.readline

# 지도
board = [[False for _ in range(6)] for _ in range(6)]

xy_list = []

for idx in range(36):
    n = input().strip()

    x, y = (ord(n[0]) - 5) % 6, int(n[1]) - 1

    xy_list.append([x, y])

# 초기 위치
prev_x, prev_y = xy_list[0][0], xy_list[0][1]
# 방문처리
board[prev_y][prev_x] = True

for i in range(1, 36):
    x, y = xy_list[i][0], xy_list[i][1]
    # 예외 처리
    if not board[y][x]:
        board[y][x] = True # 방문처리
    else:
        print("Invalid")
        exit(0)

    # 나이트가 이상하게 이동한 경우
    if prev_x + 1 == x and ( prev_y + 2 == y or prev_y - 2 == y ):
        prev_x, prev_y = x, y
        continue
    elif prev_x + 2 == x and ( prev_y + 1 == y or prev_y - 1 == y ):
        prev_x, prev_y = x, y
        continue
    elif prev_x - 1 == x and ( prev_y + 2 == y or prev_y - 2 == y ):
        prev_x, prev_y = x, y
        continue
    elif prev_x - 2 == x and ( prev_y + 1 == y or prev_y - 1 == y ):
        prev_x, prev_y = x, y
        continue
    else:
        print("Invalid")
        exit(0)

for i in range(6):
    for j in range(6):
        if board[i][j]:
            pass
        else:
            print("Invalid")
            exit(0)

# 마지막 위치에서 처음으로 갈 수 있는지 체크
if prev_x + 1 == xy_list[0][0] and ( prev_y + 2 == xy_list[0][1] or prev_y - 2 == xy_list[0][1] ):
    print("Valid")
elif prev_x + 2 == xy_list[0][0] and ( prev_y + 1 == xy_list[0][1] or prev_y - 1 == xy_list[0][1] ):
    print("Valid")
elif prev_x - 1 == xy_list[0][0] and ( prev_y + 2 == xy_list[0][1] or prev_y - 2 == xy_list[0][1] ):
    print("Valid")
elif prev_x - 2 == xy_list[0][0] and ( prev_y + 1 == xy_list[0][1] or prev_y - 1 == xy_list[0][1] ):
    print("Valid")
else:
    print("Invalid")
