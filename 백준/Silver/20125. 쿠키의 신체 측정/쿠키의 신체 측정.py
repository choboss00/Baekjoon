import sys

input = sys.stdin.readline

n = int(input())

board = [list(input().strip()) for _ in range(n)]

# 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리
left1, right1, mid, left2, right2 = 0,0,0,0,0
# 심장 위치 저장
heart_x, heart_y = 0, 0

for y in range(n):
    for x in range(n):
        # 머리 위치 찾기
        if board[y][x] == '*' and ( heart_x == 0 and heart_y == 0):
            # 심장 위치 설정
            heart_x = x+1
            heart_y = y+2
            # 탐색 ( 왼쪽, 오른쪽, 아래, 왼쪽 아래, 오른쪽 아래 )
            xx = x-1
            # 왼쪽
            while xx >= 0 and board[y+1][xx] == '*':
                left1 += 1
                xx -= 1

            xxx = x+1
            # 오른쪽
            while xxx < n and board[y+1][xxx] == '*':
                right1 += 1
                xxx += 1

            # 아래
            y3 = y+2
            while y3 < n and board[y3][x] == '*':
                mid += 1
                y3 += 1

            # 왼쪽, 오른쪽 아래
            x4, x5 = x-1, x+1
            y4, y5 = y3, y3
            while y4 < n and board[y4][x4] == '*':
                left2 += 1
                y4 += 1
            while y5 < n and board[y5][x5] == '*':
                right2 += 1
                y5 +=1

            print(heart_y, heart_x)
            print(left1, right1, mid, left2, right2)
            exit(0)