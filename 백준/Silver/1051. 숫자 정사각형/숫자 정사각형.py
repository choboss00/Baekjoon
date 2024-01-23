"""
## 숫자 정사각형

## 문제
1. N * M 크기의 직사각형
- 각 칸에는 한 자리 숫자가 적혀있음

2. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램 작성하기

3. 정사각형은 행 또는 열에 평행해야 함 ( 마름모같은건 안됨 )

## 입력
1. N, M

## 출력
1. 정사각형의 크기

## 풀이
1. 각 꼭짓점마다 동일한 숫자가 있는지 비교

2. 예시 : (0,0) 시작
- 오른쪽, 대각선, 아래 한칸씩 전진하면서 체크

"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, list(input().strip()))) for _ in range(n)]

def solve(x, y):
    answers = []

    now_x, now_y = x, y
    prev_number = board[y][x]  # 이전 숫자와 비교

    idx = 0

    while True:
        now_x = x + idx
        now_y = y + idx

        if now_x >= m or now_y >= n:
            break

        if prev_number == board[now_y-idx][now_x] and prev_number == board[now_y][now_x] and prev_number == board[now_y][now_x-idx]:
            answers.append((now_x - x + 1) ** 2)

        idx += 1

    return answers

answers = []

for y in range(n):
    for x in range(m):
        ans_list = solve(x, y)

        if len(ans_list) > 0:
            answers.append(max(ans_list))

print(max(answers))