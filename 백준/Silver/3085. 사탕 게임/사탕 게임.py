import sys

input = sys.stdin.readline

n = int(input())
# 지도 만들기
board = []

for _ in range(n):
    board.append(list(input().strip()))

# 최댓값을 저장하는 리스트
cnt_list = []

# 가장 위에서부터 탐색 진행
for y in range(n):
    for x in range(n):
        # 안바꾼 상태도 체크하기
        # 가로 체크
        x_cnt = 0
        # 왼쪽 체크
        for i in range(x, n):
            if board[y][x] == board[y][i]:
                x_cnt += 1
            else:
                break
        # 오른쪽 체크
        for i in range(x - 1, -1, -1):
            if board[y][x] == board[y][i]:
                x_cnt += 1
            else:
                break

        # 세로 체크
        y_cnt = 0
        # 윗 부분 체크
        for j in range(y, n):
            if board[y][x] == board[j][x]:
                y_cnt += 1
            else:
                break
        # 아랫부분 체크
        for j in range(y - 1, -1, -1):
            if board[y][x] == board[j][x]:
                y_cnt += 1
            else:
                break
        cnt_list.append(max(x_cnt, y_cnt))

        # 아랫부분과 자리 바꾸기
        if y != n-1 and (board[y][x] != board[y+1][x]):
            # 자리 바꾸기
            board[y][x], board[y+1][x] = board[y+1][x], board[y][x]
            # 가로 체크
            x_cnt = 0
            # 왼쪽 체크
            for i in range(x, n):
                if board[y][x] == board[y][i]:
                    x_cnt += 1
                else:
                    break
            # 오른쪽 체크
            for i in range(x-1, -1, -1):
                if board[y][x] == board[y][i]:
                    x_cnt += 1
                else:
                    break

            # 세로 체크
            y_cnt = 0
            # 윗 부분 체크
            for j in range(y, n):
                if board[y][x] == board[j][x]:
                    y_cnt += 1
                else:
                    break
            # 아랫부분 체크
            for j in range(y-1, -1, -1):
                if board[y][x] == board[j][x]:
                    y_cnt += 1
                else:
                    break

            # 원래대로 돌리기
            board[y][x], board[y + 1][x] = board[y + 1][x], board[y][x]
            cnt_list.append(max(x_cnt, y_cnt))

        # 윗부분과 자리 바꾸기
        if (y != 0) and (board[y][x] != board[y-1][x]):
            # 자리 바꾸기
            board[y][x], board[y -1][x] = board[y -1][x], board[y][x]
            # 가로 체크
            x_cnt = 0
            # 왼쪽 체크
            for i in range(x, n):
                if board[y][x] == board[y][i]:
                    x_cnt += 1
                else:
                    break
            # 오른쪽 체크
            for i in range(x - 1, -1, -1):
                if board[y][x] == board[y][i]:
                    x_cnt += 1
                else:
                    break

            # 세로 체크
            y_cnt = 0
            # 윗 부분 체크
            for j in range(y, n):
                if board[y][x] == board[j][x]:
                    y_cnt += 1
                else:
                    break
            # 아랫부분 체크
            for j in range(y - 1, -1, -1):
                if board[y][x] == board[j][x]:
                    y_cnt += 1
                else:
                    break

            # 원래대로 돌리기
            board[y][x], board[y -1][x] = board[y -1][x], board[y][x]
            cnt_list.append(max(x_cnt, y_cnt))

        # 왼쪽 부분과 자리 바꾸기
        if x != 0 and board[y][x] != board[y][x-1]:
            # 자리 바꾸기
            board[y][x], board[y][x-1] = board[y][x-1], board[y][x]
            # 가로 체크
            x_cnt = 0
            # 왼쪽 체크
            for i in range(x, n):
                if board[y][x] == board[y][i]:
                    x_cnt += 1
                else:
                    break
            # 오른쪽 체크
            for i in range(x - 1, -1, -1):
                if board[y][x] == board[y][i]:
                    x_cnt += 1
                else:
                    break

            # 세로 체크
            y_cnt = 0
            # 윗 부분 체크
            for j in range(y, n):
                if board[y][x] == board[j][x]:
                    y_cnt += 1
                else:
                    break
            # 아랫부분 체크
            for j in range(y - 1, -1, -1):
                if board[y][x] == board[j][x]:
                    y_cnt += 1
                else:
                    break

            # 원래대로 돌리기
            board[y][x], board[y][x - 1] = board[y][x - 1], board[y][x]
            cnt_list.append(max(x_cnt, y_cnt))

        # 오른쪽 부분과 자리 바꾸기
        if x != n-1 and (board[y][x] != board[y][x+1]):
            # 자리 바꾸기
            board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]
            # 가로 체크
            x_cnt = 0
            # 왼쪽 체크
            for i in range(x, n):
                if board[y][x] == board[y][i]:
                    x_cnt += 1
                else:
                    break
            # 오른쪽 체크
            for i in range(x - 1, -1, -1):
                if board[y][x] == board[y][i]:
                    x_cnt += 1
                else:
                    break

            # 세로 체크
            y_cnt = 0
            # 윗 부분 체크
            for j in range(y, n):
                if board[y][x] == board[j][x]:
                    y_cnt += 1
                else:
                    break
            # 아랫부분 체크
            for j in range(y - 1, -1, -1):
                if board[y][x] == board[j][x]:
                    y_cnt += 1
                else:
                    break

            # 원래대로 돌리기
            board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]
            cnt_list.append(max(x_cnt, y_cnt))

print(max(cnt_list))