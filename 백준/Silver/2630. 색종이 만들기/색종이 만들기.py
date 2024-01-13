"""
## 색종이 만들기

## 문제
1. 여러개의 정사각형 칸들로 이루어진 정사각형 모양의 종이

2. 각 정사각형들은 하얀색 or 파란색으로 칠해져 있음

3. 주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 함

4. 전체 종이의 크기 : N * N
- N = 2^k, 1 <= k <= 7

5. 전체 종이가 모두 같은 색으로 칠해져 있지 않은 경우, 4개의 N/2 * N/2 색종이로 나눔

6. 입력으로 주어진 종이 한 변의 길이 N, 정사각형칸의 색이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램 작성하기

## 입력
1. 전체 종이의 한 변의 길이 N
- N 은 2, 4, 8, 16, 32, 64, 128 중 하나

2. 하얀색 : 0, 파란색 : 1

## 출력
1. 잘라진 하얀색 색종이의 개수, 파란색 색종이의 개수  출력하기

## 풀이
1. 분할 정복

2. 전체일 때 검사 : 모든 색종이의 색깔이 동일해야 함

3. 4분할


"""
import sys

input = sys.stdin.readline
white_cnt, blue_cnt = 0, 0
def paper(x, y, n):
    global white_cnt, blue_cnt

    color = boards[y][x]

    for i in range(y, y+n):
        for j in range(x, x+n):
            if color != boards[i][j]:
                paper(x, y, n//2)
                paper(x, y+n//2, n//2)
                paper(x+n//2, y, n//2)
                paper(x+n//2, y+n//2, n//2)
                return

    if color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1


n = int(input())

boards = [list(map(int, input().split())) for _ in range(n)]

paper(0, 0, n)

print(white_cnt)
print(blue_cnt)


